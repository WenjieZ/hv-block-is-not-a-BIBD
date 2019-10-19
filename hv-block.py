import sys
import numpy as np

n, v = int(sys.argv[1]), int(sys.argv[2])
f = str(n) + '-' + str(v) + '.csv'

A = np.zeros((n, n), dtype='int')
for i in range(v, n-v):
    for j in range(i-v, i+v+1):
        for k in range(i-v, i+v+1):
            A[j,k] += 1

np.savetxt(f, A, fmt='%i')
print('Output file name: ' + f)
