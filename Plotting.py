import matplotlib.pyplot as plt
import matplotlib as mpl
def f(x):
    return x**2 -10
x=list(range(-10,11))
#print(x)
y = [f(i) for i in x]
#print(y)
#plt.plot(x,y,'ob')
#plt.show()
font = {'size': 15}
mpl.rc('font', **font)
plt.figure(figsize=(8,4.5))
plt.plot(x, y, 'ob', label="f1")
plt.legend()
plt.title("Quick function plot")
plt.xlim(-11,11)
plt.ylim(-20, 100)
plt.xlabel("x value")
plt.ylabel("f(x) value")
plt.savefig('f1.png')
plt.legend(loc = 9)
plt.grid(linestyle='--')
plt.show()