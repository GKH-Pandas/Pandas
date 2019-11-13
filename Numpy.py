# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:51:08 2019

@author: lenovo
"""

import numpy as np
import pandas as pd
import tensorflow as tf


holder= pd.Series([1,2,3,4], index=['a','b','c','d'], dtype='float')
print(holder[2])
print(holder)
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print (arr.shape[1])
print(arr.reshape(9,1))
print(arr[2,2])
print(np.arange(1,100,5))
print(np.random.rand (1,3,3))
print(arr.sum(axis=0))
a= np.array