import mesa

from model import Schelling


def get_happy_agents_percent(model):
    """
    Display a text count of how many happy agents there are.
    """
    return f"% of happy agents: {model.happy/model.total *100}"

def get_number_of_steps(model):
    """
    Display a text count of how many happy agents there are.
    """
    return f"Number of steps until 100% happy agents: {model.steps}"


_COLORS = [
    "Aqua",
    "Blue",
    "Fuchsia",
    "Gray",
    "Green",
    "Lime",
    "Maroon",
    "Navy",
    "Olive",
    "Orange",
    "Purple",
    "Red",
    "Silver",
    "Teal",
    "White",
    "Yellow",
]


AGENT_TYPES = {0:"Aqua",
               1:"Lime",
               2:"Red",
               3:"Teal",
               4:"Fuchsia",
               5:"Yellow",
               6:"Purple",
               7:"Orange",
               8:"Silver",
               9:"Green"}

AGENT_CONDITIONS = {"happy":"Lime",
                    "unhappy":"Red"}

def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    # portrayal = {"Filled": "true", "Layer": 0, "stroke_color":"#000000"}
    # portrayal["Color"] = "Silver"
    # portrayal["Shape"] = "rect"
    # portrayal["w"] = 1
    # portrayal["h"] = 1

    if agent is None:
        return 

    portrayal = {"Filled": "true", "Layer": 0, "stroke_color":"#000000", "Shape":"circle", "r":"0.5", "Color":AGENT_TYPES[agent.type]}
    
    # if agent.type == 0:
    #     portrayal["Shape"] = "rect"
    #     portrayal["w"] = 0.5
    #     portrayal["h"] = 0.5
    #     portrayal["Color"] = ["#FFFF00", "#FFFF99"]
    # else:
    #     portrayal["Shape"] = "circle"
    #     portrayal["r"] = 0.5
    #     portrayal["Color"] = ["#0000FF", "#9999FF"]

    # if agent.income < 500:
    #     portrayal["Color"] = "Red"
    # # elif agent.income < 1000:
    # #     portrayal["Color"] = "Lime"
    # else:
    #     portrayal["Color"] = "Cyan"

    
    
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(schelling_draw, 20, 20, 500, 500)

happy_chart = mesa.visualization.ChartModule([{"Label": "happy_pc", "Color": "Black"}])

tree_chart = mesa.visualization.ChartModule(
    [{"Label": "happy_" + str(label), "Color": color}  for (label, color) in AGENT_TYPES.items()]
)
pie_chart = mesa.visualization.PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in AGENT_CONDITIONS.items()]
)

model_params = {
    "height": 20,
    "width": 20,
    "density": mesa.visualization.Slider("Agent density", 0.8, 0.1, 1.0, 0.1), #densidade de agentes, é o que determinada a quantidade de agentes e espaços vazioss
    "homophily": mesa.visualization.Slider("Homophily", 3, 0, 8, 1), #homofilia social  é a tendência dos indivíduos de se associar e de vínculo com outros semelhantes,
    "n_types": mesa.visualization.Slider("Number of agent types", 2, 1, 10, 1), # número de classes presentes no modelo
}

server = mesa.visualization.ModularServer(
    Schelling,
    [canvas_element, get_happy_agents_percent, get_number_of_steps, happy_chart, pie_chart],
    "Schelling",
    model_params,
)
