""" Implementation of a simplex LPP algorithm
    Minimize: z=cTx
    subject to:
        Ax=b, x>=0.  """
import os
import numpy as np
from numpy import  linalg as La
os.system('clear')


A=np.array([[3,1,1,0,0],[1,2,0,1,0],[1,0,0,0,1]])
b=np.array([[10],[8],[3]])
c=np.array([-6,-7,0,0,0])
basic_set=np.array([2,3,4])
nonbasic_set=np.array([0,1])
B=A[:,basic_set]
cb=c[basic_set]

N=A[:,nonbasic_set]
cn=c[nonbasic_set]
cb_ini=cb
b_cap=b
cn_cap=cn
zz1=0
print('\n Initial Simplex Tableau\n')
print('\n--------------------------------------------------------------------------\n')
print "basic_set="
print basic_set
print 'nonbasic set='
print nonbasic_set
Initial_Table=np.concatenate((B,N,b_cap),axis=1)
print Initial_Table
Cost=np.hstack((cb,cn_cap,-zz1))
print "Cost="
print Cost
print('\n----------------Iterations Start!!!--------------------------------------\n')
MaxIter=4
count=1
while np.any(cn_cap<0):
    print('\n Iteration %d \n') %(count)
    #Determine Incoming variable!
    cnDict={}
    for i in range(len(cn_cap)):
        cnDict[nonbasic_set[i]]=cn_cap[i]
    print cnDict
    cNMin=min(cn_cap)
    cNMinIndex=min(cnDict,key=cnDict.get)
    print cNMin
    print('Incoming Variable\n')
    print cNMinIndex
    
    ACapi=np.dot(La.inv(B),A[:,cNMinIndex])
    ratio={}
    for i in range(len(ACapi)):
        if ACapi[i]>0:
            ratio[basic_set[i]]=b_cap[i]/ACapi[i]
    print ratio
    MinRatioIndex=min(ratio,key=ratio.get)
    print('Leaving Variable\n')
    print MinRatioIndex # Outgoing Variable
    #Recompute basic and non basic variable sets
    for ii in range(len(basic_set)):
        if basic_set[ii]==MinRatioIndex:
            basic_set[ii]=cNMinIndex
    
    for jj in range(len(nonbasic_set)):
        if nonbasic_set[jj]==cNMinIndex:
            nonbasic_set[jj]=MinRatioIndex

    print('Basic Set=\n')
    print basic_set
    print('Non Basic Set=\n')
    print nonbasic_set

    # Recompute B and N
    B=A[:,basic_set]
    N=A[:,nonbasic_set]
    cn=c[nonbasic_set]
    cb=c[basic_set]
    print('Updated B=\n')
    print B
    print('Updated N=\n')
    print N

    xb=np.dot(La.inv(B),b)
    print('b_cap=\n')
    b_cap=xb
    print xb
    print('y=\n')
    y=np.dot(cb.T,La.inv(B))
    print y
    print('Updated cn_cap=\n')
    cn_cap=cn.T-np.dot(y.T,N)
    print cn_cap
    z=-np.dot(cb.T,xb)
    zz=zz1+np.dot(cb.T,xb)
    print z
    print zz
    count+=1
#Exit Loop------------------

print('\n------------------Printing Optimal Solution-------------------------------\n')
print('Optimal basis=\n')
print basic_set
print('Value of basic variables=\n')
print xb
print('Objective Function value=\n')
print -zz[0]
print '\n'
print('Total number of iterations=%d\n')%(count-1)