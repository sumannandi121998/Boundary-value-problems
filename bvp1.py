#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:42:39 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp

def f(x, y): #function that return an array
    return np.vstack((y[1],-np.exp(-2*y[0])))  #we devide the eq in two part ie y'=y1 and y1'=-e^(-2y)
def bc(ya, yb):
    return np.array([ya[0]-0, yb[0]-np.log(2)]) #boundary condition of y
x = np.linspace(1,2, 100)
y_a = np.zeros((2, x.size))
y_a [0]=0 #initial guess
Y = solve_bvp(f, bc, x, y_a) #solve using scipy function
plt.plot(Y.x,Y.y[0,:],label='numerical solution') #plotting of numerical solution

x_sol= np.arange(1,2.01,0.01)
y_sol= np.loadtxt("bvp1.txt",usecols=[0]) #importing the txt file that contains y values taken from mathematica
plt.plot(x_sol, y_sol, label='numerical solution using mathematica') #plotting numerical solution taken data from mathematica
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('x vs y graph')
plt.legend()
plt.show()