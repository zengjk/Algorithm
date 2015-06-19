__author__ = 'zengjk'

from numpy import *
import string as st
from random import *
from copy import *

f = file('kargerMinCut.txt')
data = f.readlines()
data = map(st.split,data)
data = [map(st.atoi,line) for line in data]


def merge(graph,i,j):
    graph[i]=graph[i]+graph[j]
    temp=[]
    for ele in graph[i]:
        if not(ele==j or ele==i):
            temp.append(ele)
    graph[i]=temp
    graph.pop(j)
    for t1 in graph.keys():
        for t2 in xrange(len(graph[t1])):
            if graph[t1][t2]==j:
                graph[t1][t2]=i


graph={}
m=[]
for vert in data:
    graph[vert[0]] = vert[1:]
n=len(graph)
for loop in xrange(500):
    graph1 = deepcopy(graph)
    for lo in xrange(n-2):
        i = choice(graph1.keys())
        j = choice(graph1[i])
        if not i==j:
            merge(graph1,i,j)
    #len(graph1[(graph1.keys())[0]])==len(graph1[(graph.keys())[1]])
    min = len(graph1[(graph1.keys())[0]])
    if min == 0:
        print graph1.keys()
        g=graph1.copy()
    m.append(min)
