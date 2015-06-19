__author__ = 'zengjk'
from numpy import *
import string as st

f=file('QuickSort.txt')
data = [x.replace("\r\n","") for x in f.readlines()]
data = array(map(st.atoi,data))
num1=num2=num3=0

def quicksort(data):
    global num1
    n = len(data)
    if n==1 or n==0:
        return data
    pivot = 0
    i = 1
    p=data[pivot]
    for j in xrange(i,n):
        num1+=1
        if data[j] < p:
            data[i],data[j] = data[j],data[i]
            i += 1
    data[pivot],data[i-1] = data[i-1],data[pivot]
    data[:i-1] = quicksort(data[:i-1])
    if i+1<=n:
        data[i:] = quicksort(data[i:])
    return data

def quicksort2(data):
    global num2
    n = len(data)
    if n==1 or n==0:
        return data
    data[n-1],data[0] = data[0],data[n-1]
    pivot = 0
    i = 1
    p=data[pivot]
    for j in xrange(i,n):
        num2+=1
        if data[j] < p:
            data[i],data[j] = data[j],data[i]
            i += 1
    data[pivot],data[i-1] = data[i-1],data[pivot]
    data[:i-1] = quicksort2(data[:i-1])
    if i+1<=n:
        data[i:] = quicksort2(data[i:])
    return data

def quicksort3(data):
    global num3
    n = len(data)
    if n==1 or n==0:
        return data
    p1,p2,p3=data[0],data[(n-1)/2],data[n-1]
    if (p3-p2)*(p2-p1) > 0:
        data[(n-1)/2],data[0] = data[0],data[(n-1)/2]
    elif (p1-p3)*(p3-p2) > 0:
        data[n-1],data[0] = data[0],data[n-1]
    pivot = 0
    i = 1
    p=data[pivot]
    for j in xrange(i,n):
        num3+=1
        if data[j] < p:
            data[i],data[j] = data[j],data[i]
            i += 1
    data[pivot],data[i-1] = data[i-1],data[pivot]
    data[:i-1] = quicksort3(data[:i-1])
    if i+1<=n:
        data[i:] = quicksort3(data[i:])
    return data

data = quicksort2(data)
print data,num2
