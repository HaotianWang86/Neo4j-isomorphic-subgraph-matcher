# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:28:00 2019

@author: 34565
"""
from py2neo import Graph, NodeMatcher
from py2neo import Node,Relationship,Subgraph,PropertyDict,Walkable
from py2neo.ogm import *
import numpy as np
import sys
import webbrowser
import pandas as pd
import tkinter as tk



# =============================================================================
# Loading Query graph and Data graphs
# =============================================================================

def connectneo4j_graph():
    #########   local host/user/password depend on your neo4j server  ########################change here
    graph = Graph("http://localhost:7474", user="neo4j", password="neo4j")
    return graph

def format_response():
    data_graph = connectneo4j_graph()
    _str = 'save graph success!'
    node_str = 'number of nodes in data graph: {}'.format(len(data_graph.nodes))
    relationship_str = 'number of relationships in data graph: {}'.format(len(data_graph.relationships))
    final_str = node_str +'\n'+ relationship_str +'\n'+ _str
    return final_str

def cypher_load_graph(text):
    query_graph = connectneo4j_graph()
    n = query_graph.run(text).to_ndarray()
    return n

def load_datagraph(datagraph_entry):
    try:
        data_graph = connectneo4j_graph()
        ###  delete former graph
        data_graph.run("MATCH (n) DETACH DELETE n")
        ###  input datagraph
        data_graph.run(datagraph_entry)
    #    print('number of nodes in data graph: ', len(data_graph.nodes))
    #    print('number of relationships in data graph: ', len(data_graph.relationships))
        nodes = cypher_load_graph("MATCH (n) RETURN n")
        paths = cypher_load_graph("MATCH (n) MATCH (n)-[r]-() RETURN r")
        np.savetxt('datagraph_localnodes.txt',nodes,fmt='%s')   
        np.savetxt('datagraph_localpaths.txt',paths,fmt='%s')   
        datagraph_label['text'] = format_response()
    except:
        error_str = 'Did you change defaulted port, username and password the Neo4j\n'+'Make sure you open the Neo4j\n'+'Make sure you input correctly in Cypher Syntax' 
        datagraph_label['text'] = error_str

    
def load_querygraph(datagraph_entry):
    try:
        query_graph = connectneo4j_graph()
        ###  delete former graph
        query_graph.run("MATCH (n) DETACH DELETE n")
        ###  input datagraph
        query_graph.run(datagraph_entry)
    #    print('number of nodes in data graph: ', len(query_graph.nodes))
    #    print('number of relationships in data graph: ', len(query_graph.relationships))
        nodes = cypher_load_graph("MATCH (n) RETURN n")
        paths = cypher_load_graph("MATCH (n) MATCH (n)-[r]-() RETURN r")
        np.savetxt('querygraph_localnodes.txt',nodes,fmt='%s')   
        np.savetxt('querygraph_localpaths.txt',paths,fmt='%s')   
        querygraph_label['text'] = format_response() 
    except:        
        error_str =  'Did you change defaulted port, username and password the Neo4j\n'+'Make sure you open the Neo4j\n'+'Make sure you input correctly in Cypher Syntax' 
        querygraph_label['text'] = error_str
        
        
# =============================================================================
# visualize graphs in NEO4j Platform
# =============================================================================
    
def datagraph_visualize():
    #################################################
    ready_str = 'ready to visualize data graph'
    webbrowser.open("http://localhost:7474")
    str_ = format_response()   
    F_ = str_ + '\n' + ready_str
    datagraph_label['text'] = F_

def querygraph_visualize():
    ready_str = 'ready to visualize query graph'
    webbrowser.open("http://localhost:7474")
    
    str_ = format_response()   
    F_ = str_ + '\n' + ready_str
    querygraph_label['text'] = F_

# =============================================================================
# Grab nodes and egdes infos from local txt files
# =============================================================================
##############################
def load_graph_localnodes(graph):
    graph_lines = [line.rstrip('\n') for line in open(graph)]
    graph_lines = pd.DataFrame(graph_lines)
    graph_lines = graph_lines.values
    nodes_infos = []
    nodes_ = []
    for line in graph_lines:
        ###  in order to get ID and nodes separately:
        ID_ = str(line).split(':')[0]  
        ID_ = ID_.split('(')[1]         ###### store ID
        nodes_name = str(line).split(':')[1]
        nodes_name = nodes_name.split(' ')[0]     ############ store nodes 
        propertys_ = str(line).split('{')[1]
        propertys_ = propertys_.split('}')[0]
        nodes_info = {}
        nodes_info['ID'] = ID_
        nodes_info['Nodes'] =nodes_name
        nodes_info['Property'] =propertys_
        nodes_infos.append(nodes_info)
        nodes_ID = {}
        _ID = str(line).split(':')[0]  
        _ID = _ID.split('(')[1]         ###### store ID
        name_ = str(line).split(':')[-1]
        name_ = name_.split('}')[0]
#        name_ = name_.split(' ')[1]
        nodes_ID['ID'] = _ID
        nodes_ID['name'] = name_
        nodes_.append(nodes_ID)
    graph_nodes = []
    property_ = []
    for node in nodes_infos:
        node_n = node['Nodes']
        graph_nodes.append(node_n)
        property_.append(node['Property'])
    
    graph_nodes = list(set(graph_nodes))
    return graph_nodes,nodes_infos,nodes_, property_

def load_graph_localpaths(graph,nodes_infos,nodes_):
    graph_lines = [line.rstrip('\n') for line in open(graph)]
    graph_lines = pd.DataFrame(graph_lines)
    graph_lines = graph_lines.values
    paths_infos = []
    paths_ = []
    graph_relationships = []
    for line in graph_lines:
        start_nodes = str(line).split(')')[0]  
        start_nodes = start_nodes.split('(')[1]
        relationship_ = str(line).split(':')[1]  
        relationship_ = relationship_.split(' ')[0]
        graph_relationships.append(relationship_)
        typeofrelationship = str(line).split('{')[1]
        typeofrelationship = typeofrelationship.split('}')[0]   ######### sometimes type of relationship are empty
        end_nodes_ID = str(line).split('>')[1]
        end_nodes_ID = end_nodes_ID.split('(')[1]
        end_nodes_ID = end_nodes_ID.split(')')[0]
        end_nodes_list = []
        if end_nodes_ID[0]== '_': 
            for node in nodes_:
                if node['ID'] == end_nodes_ID:
                    end_nodes_list.append(node['name'])
        else:
            end_nodes_list.append(end_nodes_ID)
        end_nodes_list = list(set(end_nodes_list))
        paths_info = {}
        path_ = {}
        paths_info['start_nodes'] = start_nodes
        path_['start_nodes'] = start_nodes
        paths_info['relationship'] = relationship_
        path_['relationship'] = relationship_
        paths_info['relationship_type'] = typeofrelationship
        paths_info['end_nodes'] = str(end_nodes_list)
        path_['end_nodes'] = str(end_nodes_list)
        paths_infos.append(paths_info)
        paths_.append(path_)
    graph_relationships = list(set(graph_relationships))
    return graph_relationships, paths_infos,paths_

# =============================================================================
# Isomorphism subgraph Algorthim VF2
# =============================================================================


class DiGraphMatcher():
    """Implementation of VF2 algorithm for matching directed graphs.
    """
    def __init__(self, G1, G2):
        super(DiGraphMatcher, self).__init__(G1, G2)
    def candidate_pairs_iter(self):
        # All computations are done using the current state!
        G1_nodes = self.G1_nodes
        G2_nodes = self.G2_nodes
        # First we compute the out-terminal sets.
        T1_out = [node for node in G1_nodes if (node in self.out_1) and (node not in self.core_1)]
        T2_out = [node for node in G2_nodes if (node in self.out_2) and (node not in self.core_2)]
        # If T1_out and T2_out are both nonempty.
        # P(s) = T1_out x {min T2_out}
        if T1_out and T2_out:
            node_2 = min(T2_out)
            for node_1 in T1_out:
                yield node_1, node_2
        # If T1_out and T2_out were both empty....
        # We compute the in-terminal sets.
        ##elif not (T1_out or T2_out):   # as suggested by [2], incorrect
        else:                            # as suggested by [1], correct
            T1_in = [node for node in G1_nodes if (node in self.in_1) and (node not in self.core_1)]
            T2_in = [node for node in G2_nodes if (node in self.in_2) and (node not in self.core_2)]
            # If T1_in and T2_in are both nonempty.
            # P(s) = T1_out x {min T2_out}
            if T1_in and T2_in:
                node_2 = min(T2_in)
                for node_1 in T1_in:
                    yield node_1, node_2
            # If all terminal sets are empty...
            # P(s) = (N_1 - M_1) x {min (N_2 - M_2)}
            ##elif not (T1_in or T2_in):   # as suggested by  [2], incorrect
            else:                          # as inferred from [1], correct
                node_2 = min(G2_nodes - set(self.core_2))
                for node_1 in G1_nodes:
                    if node_1 not in self.core_1:
                        yield node_1, node_2
        # For all other cases, we don't have any candidate pairs
    def initialize(self):
        self.core_1 = {}
        self.core_2 = {}
        # See the paper for definitions of M_x and T_x^{y}
        # The value stored is the depth of the search tree when the node became
        # part of the corresponding set.
        self.in_1 = {}
        self.in_2 = {}
        self.out_1 = {}
        self.out_2 = {}
        self.state = DiGMState(self)
        # Provide a convienient way to access the isomorphism mapping.
        self.mapping = self.core_1.copy()
    def syntactic_feasibility(self, G1_node, G2_node):

        if self.G1.number_of_edges(G1_node,G1_node) != self.G2.number_of_edges(G2_node,G2_node):
            return False
        # the number of edges must be equal
        for predecessor in self.G1.pred[G1_node]:
            if predecessor in self.core_1:
                if not (self.core_1[predecessor] in self.G2.pred[G2_node]):
                    return False
                elif self.G1.number_of_edges(predecessor, G1_node) != self.G2.number_of_edges(self.core_1[predecessor], G2_node):
                    return False
        for predecessor in self.G2.pred[G2_node]:
            if predecessor in self.core_2:
                if not (self.core_2[predecessor] in self.G1.pred[G1_node]):
                    return False
                elif self.G1.number_of_edges(self.core_2[predecessor], G1_node) != self.G2.number_of_edges(predecessor, G2_node):
                    return False
        # edges must be equal.
        for successor in self.G1[G1_node]:
            if successor in self.core_1:
                if not (self.core_1[successor] in self.G2[G2_node]):
                    return False
                elif self.G1.number_of_edges(G1_node, successor) != self.G2.number_of_edges(G2_node, self.core_1[successor]):
                    return False

        for successor in self.G2[G2_node]:
            if successor in self.core_2:
                if not (self.core_2[successor] in self.G1[G1_node]):
                    return False
                elif self.G1.number_of_edges(G1_node, self.core_2[successor]) != self.G2.number_of_edges(G2_node, successor):
                    return False
        ### Look ahead 1
        # R_termin
        # The number of predecessors of n that are in T_1^{in} is equal to the
        # number of predecessors of m that are in T_2^{in}.
        num1 = 0
        for predecessor in self.G1.pred[G1_node]:
            if (predecessor in self.in_1) and (predecessor not in self.core_1):
                num1 += 1
        num2 = 0
        for predecessor in self.G2.pred[G2_node]:
            if (predecessor in self.in_2) and (predecessor not in self.core_2):
                num2 += 1
        if self.test == 'graph':
            if not (num1 == num2):
                return False
        else: # self.test == 'subgraph'
            if not (num1 >= num2):
                return False
        # The number of successors of n that are in T_1^{in} is equal to the
        # number of successors of m that are in T_2^{in}.
        num1 = 0
        for successor in self.G1[G1_node]:
            if (successor in self.in_1) and (successor not in self.core_1):
                num1 += 1
        num2 = 0
        for successor in self.G2[G2_node]:
            if (successor in self.in_2) and (successor not in self.core_2):
                num2 += 1
        if self.test == 'graph':
            if not (num1 == num2):
                return False
        else: # self.test == 'subgraph'
            if not (num1 >= num2):
                return False
        # R_termout
        # The number of predecessors of n that are in T_1^{out} is equal to the
        # number of predecessors of m that are in T_2^{out}.
        num1 = 0
        for predecessor in self.G1.pred[G1_node]:
            if (predecessor in self.out_1) and (predecessor not in self.core_1):
                num1 += 1
        num2 = 0
        for predecessor in self.G2.pred[G2_node]:
            if (predecessor in self.out_2) and (predecessor not in self.core_2):
                num2 += 1
        if self.test == 'graph':
            if not (num1 == num2):
                return False
        else: # self.test == 'subgraph'
            if not (num1 >= num2):
                return False
        # The number of successors of n that are in T_1^{out} is equal to the
        # number of successors of m that are in T_2^{out}.
        num1 = 0
        for successor in self.G1[G1_node]:
            if (successor in self.out_1) and (successor not in self.core_1):
                num1 += 1
        num2 = 0
        for successor in self.G2[G2_node]:
            if (successor in self.out_2) and (successor not in self.core_2):
                num2 += 1
        if self.test == 'graph':
            if not (num1 == num2):
                return False
        else: # self.test == 'subgraph'
            if not (num1 >= num2):
                return False
        ### Look ahead 2
        # The number of predecessors of n that are neither in the core_1 nor
        # T_1^{in} nor T_1^{out} is equal to the number of predecessors of m
        # that are neither in core_2 nor T_2^{in} nor T_2^{out}.
        num1 = 0
        for predecessor in self.G1.pred[G1_node]:
            if (predecessor not in self.in_1) and (predecessor not in self.out_1):
                num1 += 1
        num2 = 0
        for predecessor in self.G2.pred[G2_node]:
            if (predecessor not in self.in_2) and (predecessor not in self.out_2):
                num2 += 1
        if self.test == 'graph':
            if not (num1 == num2):
                return False
        else: # self.test == 'subgraph'
            if not (num1 >= num2):
                return False
        # The number of successors of n that are neither in the core_1 nor
        # T_1^{in} nor T_1^{out} is equal to the number of successors of m
        # that are neither in core_2 nor T_2^{in} nor T_2^{out}.
        num1 = 0
        for successor in self.G1[G1_node]:
            if (successor not in self.in_1) and (successor not in self.out_1):
                num1 += 1
        num2 = 0
        for successor in self.G2[G2_node]:
            if (successor not in self.in_2) and (successor not in self.out_2):
                num2 += 1
        if self.test == 'graph':
            if not (num1 == num2):
                return False
        else: # self.test == 'subgraph'
            if not (num1 >= num2):
                return False
        # Otherwise, this node pair is syntactically feasible!
        return True
    
# =============================================================================
# let the project fit for the VF2 Alogrithm (using network X python graph)
# =============================================================================    
import networkx as nx
from networkx.algorithms import isomorphism
import pandas as pd 
def isomorphism_subgraph_matching():
    querygraph_nodes = 'querygraph_localnodes.txt'
    datagraph_nodes = 'datagraph_localnodes.txt'
    datagraph_nodes,datagraph_nodes_infos,datanodes_,dataproperty_ = load_graph_localnodes(datagraph_nodes)
    querygraph_nodes,querygraph_nodes_infos,querynodes_,queryproperty_ = load_graph_localnodes(querygraph_nodes)
    datagraph_paths = 'datagraph_localpaths.txt'
    querygraph_paths = 'querygraph_localpaths.txt'
    datagraph_relationships, datagraph_paths_infos,datapath_ = load_graph_localpaths(datagraph_paths,datagraph_nodes_infos,datanodes_)
    querygraph_relationships, querygraph_paths_infos,querypath_ = load_graph_localpaths(querygraph_paths,querygraph_nodes_infos,querynodes_)
    DG=nx.DiGraph() ####### data graph
    for n in datapath_:
        start_nodes = n['start_nodes']
        edge =n['relationship']
        end_nodes = n['end_nodes']
        DG.add_edges_from([(start_nodes,end_nodes)],relationship = edge)  
    QG=nx.DiGraph() ####### query graph
    for m in querypath_:
        start_nodes = m['start_nodes']
        edge = m['relationship']
        end_nodes = str(m['end_nodes'])
        QG.add_edges_from([(start_nodes,end_nodes)],relationship = edge)
    DiGM = isomorphism.DiGraphMatcher(DG,QG)
    n= 0
    for subgraph in DiGM.subgraph_isomorphisms_iter():
        n += 1
        print(n)
    Questions = 'Is subgraph isomorphism??'
    ISanswer = DiGM.subgraph_is_isomorphic()
    ISanswer = str(ISanswer)
    print(ISanswer)
    num = 'Totally have {} isomorphism subgraph'.format(n)
    print(num)
    final_str = Questions +'\n'+ ISanswer +'\n'+ num
    matchinglabel['text'] = final_str
#isomorphism_subgraph_matching()

def isomorphism_subgraph_matching_nodes():
    querygraph_nodes = 'querygraph_localnodes.txt'
    datagraph_nodes = 'datagraph_localnodes.txt'
    datagraph_nodes,datagraph_nodes_infos,datanodes_,dataproperty_ = load_graph_localnodes(datagraph_nodes)
    querygraph_nodes,querygraph_nodes_infos,querynodes_,queryproperty_ = load_graph_localnodes(querygraph_nodes)
    datagraph_paths = 'datagraph_localpaths.txt'
    querygraph_paths = 'querygraph_localpaths.txt'
    datagraph_relationships, datagraph_paths_infos,datapath_ = load_graph_localpaths(datagraph_paths,datagraph_nodes_infos,datanodes_)
    querygraph_relationships, querygraph_paths_infos,querypath_ = load_graph_localpaths(querygraph_paths,querygraph_nodes_infos,querynodes_)
    DG=nx.DiGraph() ####### data graph
    for n in datapath_:
        start_nodes = n['start_nodes']
        edge =n['relationship']
        end_nodes = n['end_nodes']
        DG.add_edges_from([(start_nodes,end_nodes)],relationship = edge)  
    QG=nx.DiGraph() ####### query graph
    for m in querypath_:
        start_nodes = m['start_nodes']
        edge = m['relationship']
        end_nodes = str(m['end_nodes'])
        QG.add_edges_from([(start_nodes,end_nodes)],relationship = edge)
    DiGM = isomorphism.DiGraphMatcher(DG,QG)
    n= 0
    num_list = [] 
    subgraph_list = []
    output_list = []
    for subgraph in DiGM.subgraph_isomorphisms_iter():
        n += 1
        num_list.append(n)
        subgraph_list.append(subgraph)
    output_list = dict(zip(num_list,subgraph_list))
    print(output_list)
#    matchinglabel['text'] = output_list                 ###show the results of a large graph in interface takes longtime 


# =============================================================================
# GUI graphical user interface
# =============================================================================
HEIGHT = 1000
WIDTH = 1000

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
canvas.create_text(130,40, text = 'Data graph', font = ('Helvetica', 30, 'bold'), justify = 'center', fill='red')
canvas.create_text(130,190, text = 'Query graph', font = ('Helvetica', 30, 'bold'), justify = 'center', fill='red')
canvas.create_text(130,350, text = 'Isomorphism subgraph\n Matching', font = ('Helvetica', 16, 'bold'), justify = 'center', fill='red')
########  data graph function
datagraph_frame = tk.Frame(root, bg='#80c1ff', bd=5)
datagraph_frame.place(relx=0.6, rely=0.03, relwidth=0.7, relheight=0.05, anchor='n')
datagraph_entry = tk.Entry(datagraph_frame, font=40)
datagraph_entry.place(relwidth=0.65, relheight=1)
datagraph_button = tk.Button(datagraph_frame, text="Load", font=40, command = lambda: load_datagraph(datagraph_entry.get()))
datagraph_button.place(relx=0.7, relheight=1, relwidth=0.15)
datagraph_button = tk.Button(datagraph_frame, text="Visualize", font=40, command = datagraph_visualize)
datagraph_button.place(relx=0.85, relheight=1, relwidth=0.15)
datagraphanswer_frame = tk.Frame(root, bg='#80c1ff', bd=5)
datagraphanswer_frame.place(relx=0.6, rely=0.09, relwidth=0.7, relheight=0.1, anchor='n')
datagraph_label = tk.Label(datagraphanswer_frame)
datagraph_label.place(relwidth=1, relheight=1)

######### query graph function
querygraph_frame = tk.Frame(root, bg='#80c1ff', bd=5)
querygraph_frame.place(relx=0.6, rely=0.2, relwidth=0.7, relheight=0.05, anchor='n')
querygraph_entry = tk.Entry(querygraph_frame, font=40)
querygraph_entry.place(relwidth=0.65, relheight=1)
querygraph_button = tk.Button(querygraph_frame, text="Load", font=40, command = lambda: load_querygraph(querygraph_entry.get()))
querygraph_button.place(relx=0.7, relheight=1, relwidth=0.15)
querygraph_button = tk.Button(querygraph_frame, text="Visualize", font=40, command = querygraph_visualize)
querygraph_button.place(relx=0.85, relheight=1, relwidth=0.15)
querygraphanswer_frame = tk.Frame(root, bg='#80c1ff', bd=5)
querygraphanswer_frame.place(relx=0.6, rely=0.26, relwidth=0.7, relheight=0.13, anchor='n')
querygraph_label = tk.Label(querygraphanswer_frame)
querygraph_label.place(relwidth=1, relheight=1)

######### matching function
matching_frame = tk.Frame(root, bg='#80c1ff', bd=5)
matching_frame.place(relx=0.6, rely=0.4, relwidth=0.7, relheight=0.05, anchor='n')
#entry = tk.Entry(matching_frame, font=40)
#entry.place(relwidth=0.65, relheight=1)
matchingbutton = tk.Button(matching_frame, text="Matching", font=40,command = lambda: isomorphism_subgraph_matching())
matchingbutton.place(relx=0.4, relheight=1, relwidth=0.3)

matchingbutton = tk.Button(matching_frame, text="Subgraph Infos", font=40,command = lambda: isomorphism_subgraph_matching_nodes())
matchingbutton.place(relx=0.7, relheight=1, relwidth=0.3)

matchinganswer_frame = tk.Frame(root, bg='#80c1ff', bd=5)
matchinganswer_frame.place(relx=0.6, rely=0.46, relwidth=0.7, relheight=0.43, anchor='n')
matchinglabel = tk.Label(matchinganswer_frame)
matchinglabel.place(relwidth=1, relheight=1)

root.mainloop()
