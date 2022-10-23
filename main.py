import numpy as np
M = np.matrix([[0,1,1,0],
               [1,0,1,1],
               [1,1,0,1],
               [0,1,1,0]])
M2 = M*M
print(M2)