'''
Author: Lane Carasik
Purpose: Learn how to use iapws module for water properties
'''

#----------------------------------------------------------------------------------#
# import modules
from iapws import IAPWS95
# https://iapws.readthedocs.io/en/latest/modules.html#documentation
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------#
# Print Logic (if set to 0 it will save figures, if 1 it will not save.)

print_logic = 1

#----------------------------------------------------------------------------------#
# Define functions needed

def Prandtl(c_p,mu,k):
	# Prandtl number calculation
	Pr = c_p*mu/k
	
	return Pr
    
def Reynolds(rho,vel,D_h,mu):
	# Reynolds number calculation
	Re = rho*vel*D_h/mu
	
	return Re

def f_Blasius(Re):
    # Friction factor for calculating smooth pipe 
    #friction factor
    f = 0.3164*Re**(-0.25)
    
    return f

def Nu_DB(Re,Pr):
    # Nusselt number correlation (Dittus Boelter)
    # for smooth pipe flow
    # cooling so n = 0.3 or n = 0.4 for heating
	Nu = 0.023*(Re**0.8)*(Pr**0.4)

	return Nu   

#----------------------------------------------------------------------------------#
# Learning how to use iapws properties for water

H20 = IAPWS95(T=293.15,P=0.101325)
print(H20.rho,H20.nu,H20.cp,H20.k)

temp = 20+273.15 # Temperature in Kelvin
prez = 0.101325 # Pressure in MPa

H20 = IAPWS95(T=temp,P=prez)
print(H20.rho,H20.nu,H20.cp,H20.k)

u_ref = 1.1 # m/s
D_h = 0.01 # m
Re_H20 = Reynolds(H20.rho,u_ref,D_h,H20.mu)
Pr_H20 = Prandtl(H20.cp*1e3,H20.mu,H20.k)

#----------------------------------------------------------------------------------#
# Print out relevant quantities

print("Prandtl number is",np.round(Pr_H20,3))
print("Reynolds number is,",np.round(Re_H20,3))
print("Friction factor is,",np.round(f_Blasius(Re_H20),4))
print("Nusselt number is,",np.round(Nu_DB(Re_H20,Pr_H20),2))

