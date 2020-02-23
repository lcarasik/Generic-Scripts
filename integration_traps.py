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

# Define 
num = 60
z = np.linspace(-np.pi,np.pi,num)
f = np.zeros(num)
integral = np.zeros(num)

# Define the function
for i in range(0,num):
    f[i] = np.cos(z[i])

for i in range(0,num):
    integral[i] = np.trapz(f[0:i+1],z[0:i+1])

print(f[0:num])
print(integral)

'''
--------------------------------------------------------------------------------------------
--------------------------- Plot the function and integral ---------------------------------
--------------------------------------------------------------------------------------------
'''

plt.figure(1)
plt.plot(z,f,'k',label = 'Function')
plt.plot(z,integral,'r',label = 'Integral')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()