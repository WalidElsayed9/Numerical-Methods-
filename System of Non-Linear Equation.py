import numpy as np
import scipy.optimize
import sympy
import matplotlib.pyplot as plt
import matplotlib as mpl
x1, x2, x3 = sympy.symbols('x1,x2,x3')
fsym = []
fsym.append(x1**2 + x2**2 + x3**2 - 62.0)
fsym.append(x1 - x2 + x3 + 8.0)
fsym.append((x1 * x2 + x2 * x3**2 + 2)/(x1 + x3) + 31.0)
print(fsym)
x = [1,1,1]
xx = [x1,x2,x3] 
for i in range(len(fsym)):
    for j in range(len(fsym)):
        print(sympy.diff(fsym[i],xx[j]).evalf(subs={x1:x[0], x2:x[1],x3:x[2]}), end = ' ')
        
        
    #print('')    
                # '''Solve with scipy'''
def f_sc(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    f = []
    f.append(x1**2 + x2**2 + x3**2 - 62.0)
    f.append(x1 - x2 + x3 + 8.0)
    f.append((x1 * x2 + x2 * x3**2 + 2)/(x1 + x3) + 31.0)
    return f
#print(scipy.optimize.fsolve(f_sc,[1,1,1], xtol = 1e-8))
# ''''Look at the error''''
def err_val(x1,x2,x3):
    f1 = (x1**2 + x2**2 + x3**2 - 62.0)
    f2 = (x1 - x2 + x3 + 8.0)
    f3 =((x1 * x2 + x2 * x3**2 + 2)/(x1 + x3) + 31.0)
    return np.sqrt(f1**2 + f2**2 + f3**2)
    
#print(err_val(1,2,5))    
    

#x =np.arange(0,30,0.05)
#y =np.arange(0,20,0.05)
#X, Y =np.meshgrid(x,y)
#Z = np.ones(X.shape)
#Fxyz = err_val(X, Y, Z)

def user_surface_contour(X,Y,Z,x,y, filename='temp.png',title='f(x)', savefile=True,figsize=(16,9),xlab='\nx',ylab='y\n'):
    font = {'size':20}
    mpl.rc('font',**font)
    plt.figure(figsize=(16,9))
    contour = plt.contour(Z,10,linewidths=2,cmap=plt.cm.afmhot,origin = 'lower', extent=(x.min(), x.max(), y.min(),y.max()))
    plt.clabel(contour, inline=True, fmt='%5d', fontsize=18, colors ='black')
    pcol = plt.pcolor(X,Y,Z, cmap = 'jet')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.colorbar(pcol)
    plt.colorbar(contour)
    plt.title(title)
    if savefile:
        plt.savefig(filename)
              

    plt.show()  
#print(user_surface_contour(X,Y,Fxyz,x,y,title='z = 1'))
     
x = np.arange(0,5,0.05)
y = np.arange(-10,-3,0.05)
X, Y = np.meshgrid(x, y)
for i in range(3):
    Z= i*np.ones(X.shape)
    Fxyz = err_val(Z,X,Y)
    print(user_surface_contour(X,Y,Fxyz,x,y, xlab='\ny',ylab='z\n', title='$x_1= ' + str(i)+'$' , filename = str(i)+'_err.png'))
    
    