import numpy as np
import math
import scipy as sp
from scipy import linalg
import pandas as pd
import matplotlib.pyplot as plt
import sympy
#print(dir(sp.linalg))
#MATRIX CREATION 
a=np.empty((3,5))
#print(a)
v=np.zeros((4,3))
#print(v)
d=np.ones((5,8))
#print(d)
#print(np.eye(6,6))
#print(np.arange(15).reshape((3,5)))
z= lambda x: np.sin(x)
zn=np.vectorize(z)
s=zn(np.arange(9)).reshape(3,3)
#print(s)
map1 = map(math.sin, np.arange(9))
E = np.fromiter(map1, dtype = 'float').reshape(3,3)
#print(E)
#Matrix Concatenation
a=np.eye(3,3)
b=np.zeros((3,3))
c=np.ones((3,3))
#print(a+b)
#print(np.concatenate([a,b,c]))
#print(np.vstack([a,b,c]))
#Matrix - Matrix Multiplication
A = np.array([[1,2],[3,4]])
#print(np.dot(A,A))
np.random.seed(1)
A = np.ceil(10*np.random.random((4,4)))
np.random.seed(2)
B = np.ceil(10*np.random.random((4,4)))
ans = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        sum=0
        for k in range (4):
            sum = sum+ A[i,k]*B[k,j] 
            ans[i,j]=sum
            
print(ans)            
