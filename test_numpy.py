import numpy as np

a = np.arange(15).reshape(3, 5)
print('ndim', a.ndim)
print('shape', a.shape)
print('dtype', a.dtype)

print(a)
print(a[1,:])

lst = [2.1, 5.5, 81.2, -12.0]
b = np.array(lst, float)
print(b)
print('ndim', b.ndim)
print('shape', b.shape)
print('dtype', b.dtype)
