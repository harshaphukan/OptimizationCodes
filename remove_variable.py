import numpy as np
import numpy.linalg as La

for i in range(len(nonbasic_set)):
    if nonbasic_set[i]==5:
        K=np.delete(nonbasic_set,i)
N=N[:,K]
cn=cn[K]
cn_cap=cn-np.dot(y.T,N)
Initial_Table=np.concatenate((np.eye(len(B)),np.dot(La.inv(B),N),b_cap),axis=1)
Cost=np.hstack((cb,cn_cap,-zz))
print('\n----------------Table after removing artificial variable--------------\n')
print basic_set
print K
print Initial_Table
print Cost

