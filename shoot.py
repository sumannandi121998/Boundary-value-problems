#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:40:38 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def f(x,Y): #a function which return an array
    y1 = Y[0] #here y1=y
    y2 = Y[1] #y2=y'
    return [y2,-10] #we devide the eq in two part ie y'=y2 and y2'=-10
time = np.linspace(0,10,100) #devide the time interval by 100
def sol(b): #function that return sol of an initial value problem
    Y = solve_ivp(f,(0, 10),[0,b],t_eval=time)
    return Y

v=np.array([35,40,45,55,60]) #guess values of y' at t=0
for j in v:
    plt.plot(sol(j).t,sol(j).y[0,:]) #plotting of candidate solutions

z=np.empty(0)
b=0
while b<100:
    z=np.append(z,sol(b).y[0,99]) #z is an array which store the value of y at t=10 for different guess values of y'
    b=b+0.1
c=np.argmin(np.abs(z)) #it returns position of an element for which y(t=10) is close to 0
print('initial velocity',0.1*c) #printing that element
plt.plot(sol(0.1*c).t,sol(0.1*c).y[0,:]) #plotting of true numerical solution
def g(t):
    return 50*t-5*t*t #analytical sol of differential eq
t=np.arange(0,10,0.01)
plt.plot(t,g(t)) #plotting analytical solution
plt.xlim(0, 10)
plt.ylim(0, 200)
plt.xlabel('t', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('t vs y graph')
plt.legend(['initial velocity=35','initial velocity=40', 'initial velocity=45', 'initial velocity=55', 'initial velocity=60','true numerical solution','analytical solution'],fontsize=7,loc='upper left')
plt.show()
