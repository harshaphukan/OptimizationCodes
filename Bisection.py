import numpy as np
import os
import numpy.linalg as La\

def f(T):
    return (204165.5/(330-2*T))+(10400/(T-20))

def fprime(T):
    return (204165.5/(330-2*T)**2)*2-(10400/(T-20)**2)


def Bisection(a,b,eps,delx):
    count=0
    Error=9000
    while Error>eps:
        alpha=0.5*(a+b)
        fpa=fprime(a)
        fpalpha=fprime(alpha)
        if fpa*fpalpha<0:
            b=alpha
        else:
            a=alpha
    
        Error=np.abs(a-b)
        count+=1
    xOpt=a
    fOpt=f(a)
    return xOpt,fOpt,count,Error

    
xOpt,fOpt,count,Error=Bisection(40,90,1e-5,1e-2) 
print xOpt
print fOpt
print count
print Error