""" Implementation of an algorithm using the Interior-Point (Affine Scaling) Method"""
import numpy as np
import numpy.linalg as La
import os
os.system('clear')

    

A=np.array([[3,1],[1,2],[1,0]])
b=np.array([[10],[8],[3]])
c=np.array([[6],[7]])
x=np.array([[0.],[0.]])
print('Initial Value of Point Chosen=\n')
print x
gamma=0.9
eps=1e-5
z_init=np.dot(c.T,x)
print('Initial value of Objective Function=\n')
print z_init
zError=9000
i=0

while zError>=eps:
    vk=b-np.dot(A,x)
    dv=np.zeros((len(vk),len(vk)))
    for j in range(len(dv)):
        dv[j,j]=vk[j]
    D1=La.inv(np.dot(dv,dv))
    hx=np.dot(D1,A)
    hx=np.dot(A.T,hx)
    hx=La.inv(hx)
    hx=np.dot(hx,c)
    hv=-np.dot(A,hx)
    L=[]
    for ii in range(len(hv)):
        if hv[ii]<0:
            L.append(-vk[ii]/hv[ii])
        else:
            L.append(float('Inf'))
    alpha=gamma*min(L)[0]
    K= alpha*hx
    x=x+K
    z=np.dot(c.T,x)
    zError=np.abs(z-z_init)
    z_init=z
    i+=1

print ('\n--------Printing Optimal Solution---------------------\n') 
print('Optimal Value of Objective Function=\n')
print np.dot(c.T,x)[0][0]
print('Optimal value of Objective Function exists at x=\n')
print x
print('Relative error=\n')
print zError[0][0]
print('Number of iterations=%d\n') %(i)
