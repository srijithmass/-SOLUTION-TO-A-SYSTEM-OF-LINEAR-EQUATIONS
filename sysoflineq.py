#Program to find the solution for the given linear equations.
#Developed by: SRIJITH R
#RegisterNumber: 21004191

import numpy as np
x=np.array([[5,-3,-10],[2,2,-3],[-3,-1,5]])
y=np.array([-9,4,-1])
value=np.linalg.solve(x,y)
print(value)