import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import scipy as sp
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import sympy
x=np.linspace(1,100,10)
y=np.log(x)
df=pd.DataFrame(np.c_[x,y],columns=['x','y'])
print(df.head())
df.plot.scatter('x','y')
plt.show()