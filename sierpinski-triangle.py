#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:13:54 2019

@author: sazd3
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

x0=[0.5,-.5,0]
y0=[0,0,np.sqrt(5)/4]
x=x0
y=y0
newx=(x[0]+x[1])/2
newy=(y[0]+y[1])/2
n=100000 #number of points
for i in range(n):
    p1=np.random.randint(0,3)
    print(p1,x0[p1],y0[p1])
    x.append((x0[p1]+newx)/2)
    y.append((y0[p1]+newy)/2)
    newx=x[-1]
    newy=y[-1]
    
plt.scatter(x,y,s=.2)
    
