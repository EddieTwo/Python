# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
a = np.array([[0, 1], [-1, 0]], dtype = np.float64) 
print('a', a)
print('a squared', np.multiply(a, a))

b = np.ones((2, 2))
print('b', b)

c = np.eye(2)
print('c', c)

# eigenvalues
ei = np.linalg.eig(a)
print('eigenvalues', ei)

# broadcasting
x = np.array([1.j, -1.j])
print('x', x)
print('a + x', a + x)


