import numpy as np

# two dim array
a = np.arange(15).reshape(3, 5)

print('ndim', a.ndim)
print('shape', a.shape)
print('dtype', a.dtype)
print(a)
print(a[1,:])
print()

# one dimentional array
lst = [2.1, 5.5, 81.2, -12.0]
b = np.array(lst, float)
print(b)
print('ndim', b.ndim)
print('shape', b.shape)
print('dtype', b.dtype)
print()

# numpy dates
dt = np.array(['2015-01-13', '2015-02-13', '2015-05-13', '2015-06-13'], dtype='datetime64')
print(dt)

dlt = np.diff(dt)
print(dlt.dtype)
print(dlt)

c = dlt/np.timedelta64(1, 'D')
print(c.dtype)
print(c)

dt2 = np.cumsum(dlt) + np.datetime64('2015-01-13')
print(dt2)
print()

# more numpy dates
adt = np.datetime64('2015-01-13')
adt2 = np.datetime64('2015-02-13')
print(adt, adt2)
print(adt2 - adt, type(adt2 - adt))

# some timedelta stuff

