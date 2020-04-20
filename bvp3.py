#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:43:01 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp

def f(x, y): #function that return an array
    return np.vstack((y[1], -(2*(y[1]**3)+y[0]*y[0]*y[1])/np.cos(x)))  #we devide the eq in two part ie y'=y1 and y1'=-(2y1^3+y1*y^2)sec(x)
def bc(ya, yb):
    return np.array([ya[0]-pow(2,-1/4), yb[0]-0.5*pow(12,1/4)]) #boundary condition of y
x = np.linspace( np.pi/4, np.pi/3, 100)
y_a = np.zeros((2, x.size))
y_a [0]=1 #initial guess
Y = solve_bvp(f, bc, x, y_a) #solve using scipy function
plt.plot(Y.x,Y.y[0,:],label='numerical solution') #plotting of numerical solution

x_sol= np.arange(np.pi/4, np.pi/3,0.01)
y_sol= np.loadtxt("bvp3.txt",usecols=[0]) #importing the txt file that contains y values taken from mathematica
plt.plot(x_sol, y_sol, label='numerical solution using mathematica') #plotting numerical solution taken data from mathematica
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('x vs y graph')
plt.legend()
plt.show()