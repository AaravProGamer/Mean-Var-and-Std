import numpy as np

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

print(np.mean(mat, axis = 1))
print(np.var(mat, axis = 0))
print(np.std(mat, axis = None))



