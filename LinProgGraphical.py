import os
import numpy as np
from numpy import linalg as La
import matplotlib.pyplot as plt
os.system('clear')
x=np.linspace(0,10,100)
y=4-2*x
y1=(-2+2*x)/4.0
y3=6.0*np.ones((len(x),1))
y4=-8+2*x
y5=-2+2*x
plt.plot(x,y,'k')
plt.plot(x,y1,'r')
plt.plot(x,y3,'m')
plt.plot(x,y4,'g')
plt.plot(x,y5,'c')
plt.axis('square')
plt.ylim([0,7])
plt.xlim([0,8])
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
plt.show()