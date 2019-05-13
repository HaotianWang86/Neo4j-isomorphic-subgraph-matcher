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
* [Pandas](https://pandas.pydata.org/) - an open source data analysis library

## Starting playing the graphical user interface

A step by step series of examples that tell you how to get a development env running

Say what the step will be

### 1. Download the 'finalGUI.py' to D:\ drive. 

### 2. Following Python packages need to be installed 
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

### 3. Download the Neo4j Enterprise version.

* [Neo4j](https://neo4j.com/download/) - Neo4j enterprise instance Download

### 4. Open the Neo4j Enterprise version and create an graph port in Neo4j:

[create port](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/neo4j.PNG)

### 5. Run the interface

Issue the following command in the Anaconda command prompt/terminal with correct directorys:
```
python finalGUI.py
```
[Run the interface in Terminal](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/start_interface.PNG)<br />
After running above command, will jump out a following graphical user interfal (GUI)

![A interface screenshot](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/interface_v2.PNG)

Also, you can run the code in a Python IDE, such as SPYDER, PYCHARM without input directories.

### 6. Neo4j port information <br />
You may need to change port information in Neo4j, if you are not using a defaulted port in neo4j <br />
Defaulted Neo4j port: "http://localhost:7474" <br />
Username: neo4j <br />
Password: neo4j <br />

If needed
change the defaulted Neo4j port information, username and password: <br />
https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/38ffec01f4c1b02768ed19f64670e11da88dd31e/finalGUI.py#L24
change the defaulted Neo4j port information in visualization function: <br />
https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/38ffec01f4c1b02768ed19f64670e11da88dd31e/finalGUI.py#L85 <br />
and <br />
https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/38ffec01f4c1b02768ed19f64670e11da88dd31e/finalGUI.py#L92


### 7. Generate the Data graph <br />
Input the desired Data graph by using Cypher querying language in Data graph textbox. <br />
[Data graph textbox](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/datagraphbox.PNG)<br />
load the data graph may takes 2-3 mins, due to interface's responding time is not excellent

### 8. Visualize the data graph<br />
Click visualize button in data graph textbox, call the neo4j data visualization tool<br />
[Visualize a sample data graph](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/datagraphvisualize.PNG)

### 9. Generate the Query graph<br />
Input the desired query graph by using Cypher querying language in Data graph textbox. <br />
[Data graph textbox](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/querygraphbox.PNG)

### 10. Visualize the query graph<br />
Click visualize button in query graph textbox, call the neo4j data visualization tool<br />
[Visualize a sample query graph](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/visualizequerygraph.PNG)

### 11. Isomorphism subgraph Matching<br />
Click matching button in matching textbox, call the VF2 algorithm judge is a isomorphic subgraph or not and calculates all number of matching subgraphs.<br />
[a sample matching output](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/matchingoutput.png)

### 12. Isomorphism subgraph informations<br />
Click subgraph information button in matching textbox, call the VF2 algorithm return all the query subgraph's nodes and the matching data graph's nodes<br />
Parts of information, start from No.5030 isomorphic subgraph to No.5040 isomorphic subgraph<br />
[a sample information output](https://github.com/HaotianWang86/Neo4j-isomorphic-subgraph-matcher/blob/master/figures/matchingnodes.png)

## Py2neo Tutorial

[py2neo](https://nicolewhite.github.io/neo4j-jupyter/hello-world.html)


## Authors

* **Haotian Wang** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

