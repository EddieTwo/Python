import numpy as np

# two dim array
a = np.arange(15).reshape(3, 5)
print('ndim', a.ndim)
print('shape', a.shape)
print('dtype', a.dtype)

print(a)
print(a[1,:])

# one dimentional array
lst = [2.1, 5.5, 81.2, -12.0]
b = np.array(lst, float)
print(b)
print('ndim', b.ndim)
print('shape', b.shape)
print('dtype', b.dtype)

# array of dates
dt = np.array(['2007-07-13', '2006-01-13', '2010-08-13', '2010-08-13'], dtype='datetime64')
print(dt)

dlt = np.diff(dt)
print(dlt.dtype)
print(dlt)

dt2 = np.cumsum(dlt) + np.datetime64('2007-07-13')
print(dt2)

dt2 + np.timedelta64(5, 'D')

# some timedelta stuff

