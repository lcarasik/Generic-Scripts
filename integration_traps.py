'''
Title: Integration of functions in python
Author(s): Lane Carasik
Purpose: Calculate the integral of functions using python NumPy/SciPy trapz integration tool
'''

'''
--------------------------------------------------------------------------------------------
---------------------------------- Import Modules ------------------------------------------
--------------------------------------------------------------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt

'''
--------------------------------------------------------------------------------------------
--------------------------------- Define functions -----------------------------------------
--------------------------------------------------------------------------------------------
'''

# Define the x axis
num = 60
x = np.linspace(-np.pi,np.pi,num)

# Intialize the function and integral arrays
f = np.zeros(num)
integral = np.zeros(num)

# Define the function and integral
for i in range(0,num):
    f[i] = np.cos(x[i])
for i in range(0,num):
    integral[i] = np.trapz(f[0:i+1],x[0:i+1])

'''
--------------------------------------------------------------------------------------------
--------------------------- Plot the function and integral ---------------------------------
--------------------------------------------------------------------------------------------
'''

plt.figure(1)
plt.plot(x,f,'k',label = 'Function')
plt.plot(x,integral,'r',label = 'Integral')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()