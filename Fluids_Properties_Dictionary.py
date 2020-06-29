#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:50:11 2019

@author: leninixcot
"""

#Dictionary of Fluids and properties (density, Specific Heat, Viscosity, and Thermal Conductivity)
# type dictionary name in iPython counsel to get properties 
# to get specific property -> type DictionaryName['Property'] in the iPython Counsel
#Example : Ethanol['density']
#Output: '0.7892 g/cm3'

Water = {'density': '1g/cm3' ,
         'Specific Heat': '4.179J/g-°C' ,
         'Viscosity': '8.90 × 10−4 Pa',
         'Thermal Conductivity': '0.6 W/mK'} 

Ethanol = {'density': '0.7892 g/cm3' ,
         'Specific Heat': '2.46 J/g-°C' ,
         'Viscosity': '0.001095 Pa s',
         'Thermal Conductivity': '0.171 W/m-K'}


Dichloromethane = {'density': '1.3266 g/cm3',
       'Specific Heat': '1.188 J/g-°C',
       'Viscosity': '0.43 cP',
       'Thermal Conductivity': '0.1392 W/m-K'}

print(Water)

print(Ethanol)

print(Dichloromethane)



