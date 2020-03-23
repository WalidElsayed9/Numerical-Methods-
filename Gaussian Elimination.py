import numpy as np
import math
import scipy as sp
from scipy import linalg
import pandas as pd
import matplotlib.pyplot as plt
import sympy

np.random.seed(2)
a = np.ceil(10*np.random.random((4,4)))
#print(a)
b = np.floor(10*np.random.random((4,1)))
#print(b)
A = np.hstack((a,b))
#print(A)
#print(A.shape[0])
N = A.shape[0]
for k in range(N-1):
    for i in range (k+1,N):
        r = -A[i,k] / A[k,k]
        for j in range (k+1,N+1):
            A[i,j] = A[i,j] + r*A[k,j]
            
        for j in range(k+1):
            A[i,j] = 0
            

#print(A)  
            '''BACK SUBSTITUTION''' 
A[N-1,N] = A[N-1,-1] / A[N-1, -2]
for i in range(N-2, -1, -1):
    sum = 0
    for j in range(i+1,N):
        sum = sum +A[i,j] * A[j,N]
    A[i,N] = (A[i,N]-sum)/A[i,i]
print(A[:,N])    
            
        
        