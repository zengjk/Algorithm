__author__ = 'zengjk'
from collections import *
class graph:
    def __init__(self):
        self.node=set()
        self.edge=defaultdict(list)
        self.distance = {}
    def add_node(self,value):
        self.node.add(value)
    def add_edge(self,from_node,to_node,distance):
        self.edge[from_node].append(to_node)
        self.edge[to_node].append(from_node)
        self.distance[(from_node,to_node)] = distance

def dijkstra(graph, initial):
    visited = {initial:0}
    path = {}
    nodes = set(graph.node)

    while nodes:
        
