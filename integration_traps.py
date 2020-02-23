
import numpy as np
import matplotlib.pyplot as plt

num = 60
z = np.linspace(-np.pi,np.pi,num)
fluxpro = np.zeros(num)
for i in range(0,num):
    fluxpro[i] = np.cos(z[i])

integral = np.zeros(num)
for i in range(0,num):
    integral[i] = np.trapz(fluxpro[0:i+1],z[0:i+1])

print(fluxpro[0:num])
print(integral)

plt.figure(1)
plt.plot(z,fluxpro,'k',label = 'Flux Profile')
plt.plot(z,integral,'r',label = 'Integral')
plt.legend()
plt.show()