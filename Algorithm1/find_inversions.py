__author__ = 'zengjk'
from numpy import *
import string as st

f=file('IntegerArray.txt')
data = [x.replace("\r\n","") for x in f.readlines()]
data = array(map(st.atoi,data))
def Calc_Inversions(data):
    n = len(data)
    if n==1:
        return 0,data
    else:
        l, s1 = Calc_Inversions(data[:n/2])
        r, s2 = Calc_Inversions(data[n/2:])
        s, sorted = Add_Split(s1,s2)
        return l + r + s, sorted
def Add_Split(a,b):
    num = 0
    i = j = k = 0
    na = len(a)
    nb = len(b)
    sorted = zeros(na+nb)
    while i<na and j<nb:
        if a[i] > b[j]:#Found a group of inversion
            sorted[k] = b[j]
            num += na - i
            j += 1
            k += 1
        elif a[i] < b[j]:
            sorted[k] = a[i]
            i += 1
            k += 1
    if i<na:
        sorted[k:] = a[i:]
    else:
        sorted[k:] = b[j:]
    return num,sorted
num,sorted = Calc_Inversions(data)
print num











