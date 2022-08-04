from asyncio.windows_events import NULL
import mesa
from random import randint

class SchellingAgent(mesa.Agent):
    """
    Schelling segregation agent
    """

    def __init__(self, pos, model, agent_type):
        """
        Create a new Schelling agent.

        Args:
           unique_id: Unique identifier for the agent.
           x, y: Agent initial location.
           agent_type: Indicator for the agent's type (minority=1, majority=0)
        """
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type
        self.condition = "unhappy"

    def step(self):
        similar = 0
        diff = 0

        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1
            else:
                diff += 1 

        # If unhappy, move:
        if similar < self.model.homophily:           
            self.model.grid.move_to_empty(self)
            self.condition = "unhappy"
        else:
            self.model.happy += 1
            self.condition= "happy"


class Schelling(mesa.Model):
    """
    Model class for the Schelling segregation model.
    """

    def __init__(self, width=20, height=20, density=0.8, homophily=3, n_types=2):
        """ """

        self.width = width
        self.height = height

        self.density = density
        self.homophily = homophily
        self.n_types = n_types

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        # Set up agents
        # We use a grid iterator that returns
        # the coordinates of a cell as well as
        # its contents. (coord_iter)
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                agent_type = randint(0, self.n_types-1)
                agent = SchellingAgent((x, y), self, agent_type)
                self.grid.position_agent(agent, (x, y))
                self.schedule.add(agent)

        self.happy = 0
        self.steps = 0
        self.total = self.schedule.get_agent_count()

        variables = {
                "happy": lambda m: self.count_condition(m, "happy"), # Model-level count of happy agents
                "unhappy": lambda m: self.count_condition(m, "unhappy"), # Model-level count of unhappy agents
                "happy_pc": lambda m: self.get_happy_pc(m),
            }

        for t in range(0, self.n_types):
            variables["happy_"+str(t)] = lambda m: self.count_happy_pc_per_type(m, t)

        self.datacollector = mesa.DataCollector(
            variables,  
        )
        self.running = True
        self.datacollector.collect(self)
        

    def step(self):
        """
        Run one step of the model. If All agents are happy, halt the model.
        """
        self.happy = 0  # Reset counter of happy agents
        self.steps += 1
        self.schedule.step()

        # collect data
        self.datacollector.collect(self)

        # stop if all agents are happy
        if self.happy == self.schedule.get_agent_count():
            self.running = False

        # stop if model gets to 500 steps
        if self.steps >= 500:
            self.running = False
            self.steps = None
        

    @staticmethod
    def count_condition(model, agent_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for agent in model.schedule.agents:
            if agent.condition == agent_condition:
                count += 1
        return count

    @staticmethod
    def count_happy_pc_per_type(model, agent_type):
        """
        Helper method to count trees in a given condition in a given model.
        """
        total = 0
        happy = 0
        for agent in model.schedule.agents:
            if agent.type == agent_type:
                total += 1
                if agent.condition == "happy":
                    happy += 1
        return happy/total *100

    @staticmethod
    def get_happy_pc(model):
        return model.happy/model.total *100
