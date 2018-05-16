import numpy as np
import os
import numpy.linalg as La
os.system('clear')

def f(T):
    return (204165.5/(330-2*T))+(10400/(T-20))

def GoldenSection(a,b,eps,tau):
    
    Error=9000
    count=0
    alpha1=a*(1-tau)+b*tau
    alpha2=a*tau+b*(1-tau)
    falpha1=f(alpha1)
    falpha2=f(alpha2)
    print('\n a            b\n')
    print('\n-----------------\n')
    while Error>eps:
        print('\n%7.4f    %7.4f\n') %(a,b)
        if falpha1>falpha2:
            a=alpha1
            alpha1=alpha2
            falpha1=falpha2
            alpha2=a*tau+b*(1-tau)
            falpha2=f(alpha2)
        else:
            b=alpha2
            alpha2=alpha1
            falpha2=falpha1
            alpha1=a*(1-tau)+b*tau
            falpha1=f(alpha1)
        Error=np.abs(f(alpha1)-f(alpha2))
        count+=1
        
        
    
    xOpt=alpha1
    fOpt=f(alpha1)
    return xOpt,fOpt,count,Error


    
xOpt,fOpt,count,Error=GoldenSection(40,90,1e-5,0.381967) 
print xOpt
print fOpt
print count
print Error    
    