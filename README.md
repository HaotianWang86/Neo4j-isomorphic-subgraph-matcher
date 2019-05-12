# Neo4j-isomorphic-subgraph-matcher

Neo4j and Python Interface for matching isomorphism subgraph of data graph

## Getting Started

'Neo4j - isomorphic Subgraph matcher' is a U of I Database Management System Design project. These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Neo4j enterprise instance: It's a graph database platform help to input and load datagraph and query graph
* [Neo4j](https://neo4j.com/download/) - Neo4j enterprise instance Download
* [Py2neo](https://pypi.org/project/py2neo/) - Py2neo working with Neo4j from within Python
* [webbrowser](https://docs.python.org/2/library/webbrowser.html) - webbrowser connecting web from within Python
* [NetworkX](https://networkx.github.io/) - NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks

## Starting playing the graphical user interface

A step by step series of examples that tell you how to get a development env running

Say what the step will be

1. Download the 'finalGUI.py' to D:\ drive. 

2. Following Python packages need to be installed if already not installed 
Run following command in terminal
Downloading networkx - A graph package in Python programming language
```
pip install networkx
```
Downloading webbrowser - A web browser in Python
```
python -m webbrowser -t "http://www.python.org"
```
Downloading pandas - A data analysis tool help to save the graph to local
```
pip install pandas 
```
Downloading py2neo - A python package help to edit the Neo4j Graph
```
pip install py2neo
```

3. Download the Neo4j Enterprise version.
* [Neo4j](https://neo4j.com/download/) - Neo4j enterprise instance Download

4. Open the Neo4j Enterprise version and create an graph port in Neo4j:
[create port](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/neo4j.PNG)

5. Run the interface - issue the following command in the Anaconda command prompt/terminal with correct dirs:
```
python finalGUI.py
```
[A interface screenshot](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/interface.PNG)

Also, you can run the code in a Python IDE, such as SPYDER, PYCHARM.

6. Generate the Data graph


7. Visualize the data graph


8. Generate the Query graph


9. Visualize the query graph


10. Isomorphism subgraph Matching

### Create your own Data graph port in Neo4j Desktop

1. open Neo4j enterprise instance, create a graph database. 
[create graph](https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/master/fig/create%20graph.PNG)

2. Start Running data graph 

3. Check the port informations. [port informations](https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/master/fig/HTTP%20port.PNG)

4. Change the Neo4j Port information, User name and Password in interface. 

## Loading Graphs
### Create your own Data graph port in Neo4j Desktop

1. open Neo4j enterprise instance, create a graph database. 
[create graph](https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/master/fig/create%20graph.PNG)

2. Start Running data graph 

3. Check the port informations. [port informations](https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/master/fig/HTTP%20port.PNG)

4. Change the Neo4j Port information, User name and Password in interface. 

(Different Users may have different ports)
Copy the HTTP port information to python interface. To this line:
https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/c173f78ee84963b28abc754f4769193fea1ac7c7/matchingsubgraph.py#L18
and this line:
https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/811903f8be684b54b467cf4de898c849fbcc4aae/matchingsubgraph.py#L38

### Input Data graph in Neo4j Platform:

Run following command in terminal
```
python matchingsubgraph.py inputdatagraph
```

1. Interface help to connect with Neo4j.

2. Edit the data graph in Neo4j.

We prodive a sample data graph.
[IMDB Movie data graph samples](https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/master/samples/datagraph_samples/datagraph)

### Load Data graph into python interface:
Run following command in terminal
```
python matchingsubgraph.py loaddatagraph
```

### Create your own query graph port in Neo4j Desktop

Follow above steps 1-3 to create a query graph. 

4. Change the query graph's port information, User name and Passwordin interface.

Copy the HTTP port information to python interface. To this line:
https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/811903f8be684b54b467cf4de898c849fbcc4aae/matchingsubgraph.py#L23
and this line;
https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/811903f8be684b54b467cf4de898c849fbcc4aae/matchingsubgraph.py#L53

### Input query graph in Neo4j Platform:

Run following command in terminal
```
python matchingsubgraph.py inputquerygraph
```

1. Interface help to connect with Neo4j.

2. Edit the data graph in Neo4j.

We prodive serval samples DEMO query graph.
[Query Graph DEMOs](https://github.com/HaotianWang86/NEO4J-subgraphmatcher/blob/master/samples/querygraph_samples/querygraph_test)

### Load query graph into python interface:

Run following command in terminal
```
python matchingsubgraph.py loadquerygraph
```


## Subgraph Matching

Run following command in terminal
```
python matchingsubgraph.py subgraphmatching
```


## Py2neo Tutorial

[py2neo](https://nicolewhite.github.io/neo4j-jupyter/hello-world.html)


## Authors

* **Haotian Wang** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

