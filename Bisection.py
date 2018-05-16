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
    print('\n   a       b \n')
    while Error>eps:
        print('\n  %7.4f      %7.4f \n') %(a,b)
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
print('\n-------------Printing Optimal Solution----------\n') 
print ('\n x*=%7.4f \n') %(xOpt)
print ('\n Minimum=%7.4f \n') %(fOpt)
print ('\n Number of Function Calls=%d \n') %(count)
print ('\n Final Error=%e \n') %(Error) 