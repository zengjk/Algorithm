__author__ = 'zengjk'

from numpy import *
import string as st
from random import *
from copy import *
import gc
gc.disable()
def gen_graph(data,order):
    graph={}
    if order==0:#right order
        a,b=0,1
    else:
        a,b=1,0#inv order
    for arc in data:
         if graph.has_key(arc[a]):
             graph[arc[a]].append(arc[b])
         else:
             graph[arc[a]]=[arc[b]]
         if not graph.has_key(arc[b]):
             graph[arc[b]]=[]
    return graph

marked=[]
marked2=[]
def DFS(graph,i):
    a=1
    global marked
    m=[]
    stack=[]
    stack.append(i)
    m.append(i)
    detector = i
    while len(stack)>0:
        for node in graph[detector]:
        #    print detector,node
            if not ((node in marked) or (node in m)):
                stack.append(node)
        detector = stack.pop()
        m.append(detector)
    if m[-1]==i:
        m.pop()
    return m

def DFS2(graph,i):
    global marked2
    m=[]
    a=0
    stack=[]
    pointer=0
    #stack[pointer]=i
    stack.append(i)
    m.append(i)
    detector = i
    while len(stack)>0:
        for node in graph[detector]:
            if not ((node in marked2) or (node in m)):
                #stack[pointer]=node
                stack.append(node)
                #pointer+=1
        #pointer-=1
        detector = stack.pop()
        a+=1
        print a
        m.append(detector)
    if m[-1]==i:
        m.pop()
    return m

def DFS_loop(graph):
    global marked
    for node in graph.keys():
        if not node in marked:
            marked=DFS(graph,node)+marked
            print marked

print 'Reading data...'
f = file('SCC.txt')
data = f.readlines()
data = map(st.split,data)
print 'Done!'
data = [map(st.atoi,line) for line in data]
SCC=[]
#data = [['1','7'],['2','5'],['3','9'],['4','1'],['5','8'],['6','3'],['6','8'],['7','9'],['7','4'],['8','2'],['9','6']]
print 'Generating reversed graph...'
graph_rev = gen_graph(data,1)#inv order
print 'Done!'
print len(graph_rev.keys())
print 'DFS for reversed graph...'
DFS_loop(graph_rev)
print 'Done!'
graph_rev.clear()
print 'Generating graph...'
graph = gen_graph(data,0)
print 'Done!'
print 'Calculating Strong Connected Components...'
for node in marked:
    if not node in marked2:
        SCC_temp=DFS2(graph,node)
        marked2 = SCC_temp+marked2
        SCC.append(SCC_temp)
print 'Done!'
print 'Calculating the lengths of SCCs...'
length = map(len,SCC)
print length

