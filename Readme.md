# Schelling Social Segregation

## Apresentação do novo modelo

O código inicial da simulação foi obtido a partir do repositório de exemplos da ferramenta Mesa. (https://github.com/projectmesa/mesa/tree/main/examples/schelling) 

A simulação visa reconstruir o fenômeno da segregação abordado por Schelling. Para tal, o modelo consiste em agentes que são distribuídos em um \textit{grid}, onde cada célula pode conter no máximo um agente. Inicialmente os agentes podiam pertencer a duas classes, os vermelhos e os azuis. A felicidade de um agente é obtida se um certo número de seus oito possíveis vizinhos são da mesma cor, e infelizes do contrário. Em cada etapa, agentes infelizes escolherão uma célula vazia aleatória para se moverem até que estejam felizes. O modelo continua em execução até que não haja agentes insatisfeitos. A fim de se experimentar a relação entre um número maior de classes e a quantidade de agentes felizes, foi preciso realizar algumas mudanças no código do simulador, a quais serão descritas em mais detalhes na seção "Mudanças realizadas".

## Descrição da hipótese

A hipótese causal é de que quanto maior o número de classes nas quais os indivíduos se dividem, maior é a dificuldade de se alcançar a felicidade de todos os agentes. Para que mais agentes fiquem contentes com sua vizinhança, é necessário ser mais flexivel em relação a taxa de homofilia. 

## Mudanças realizadas

- Adicionou-se a variável independente \textit{Number of agent types} para expandir e determinar o número de classes presentes no modelo;
- Adaptou-se a forma como era feita a distribuição de classes, no momento, a distribuição é feita de forma aleatória, até alcançar a densidade especificada pela variável \textit{density};
- Foram adicionadas mais cores para se representar as diversas classes; 
- A variável dependente \textit{happy} foi transformada na variável dependente \textit{Percentage of happy agents} a fim de que ela represente uma condição mais coletiva do modelo.

## Como usar o simulador

### Dependências
 
Para a execução correta do modelo deve-se instalar o pacote **mesa** e os outros listados em **requirements.txt**. Isso pode ser feito ao se executar o seguinte comando:

```
  $ pip install -r requirements.txt

```

### Execução

Para utilizar o simulador e rodar o novo modelo, basta executar o seguinte comando: 

```
    $ mesa runserver
```

## Descrição das variáveis do modelo

### Variáveis Independentes ou de Controle

- **Agent density:** densidade de agentes, é o que determinada a quantidade de agentes e espaços vazios;
- **Homophily:** em português, homofilia social, é a tendência dos indivíduos de se associar e de estabelecer vínculos com outros semelhantes;
- **Number of agent types:** número de classes dos indivíduos do modelo, classe seria o grupo com o qual o indivíduo mais se identifica.


### Variáveis Dependentes

- **Percentage of happy agents:** porcentagem de agentes felizes naquele passo, calculado pelo número de agentes que estão felizes com a sua vizinhança dividido pelo número total de agentes; 
- **Number of steps until 100\% happy agents:** número de passos que foram executados até se conseguir que todos os agentes estivessem contentes com suas respectivas vizinhanças. 
