'''
Dictionary of Fluids and properties (density, Specific Heat, Viscosity, and Thermal Conductivity)
type dictionary name in iPython counsel to get properties 
to get specific property -> type DictionaryName['Property'] in the iPython Counsel
Example : Ethanol['density']
Output: '0.7892 g/cm3'
'''

# How to define a dictonary for water
Water = {'density': '1g/cm3' ,
         'Specific Heat': '4.179J/g-°C' ,
         'Viscosity': '8.90 × 10−4 Pa',
         'Thermal Conductivity': '0.6 W/mK'} 

# How to define a dictonary for ethanol
Ethanol = {'density': '0.7892 g/cm3' ,
         'Specific Heat': '2.46 J/g-°C' ,
         'Viscosity': '0.001095 Pa s',
         'Thermal Conductivity': '0.171 W/m-K'}

# How to define a dictonary for Dichloromethane
Dichloromethane = {'density': '1.3266 g/cm3',
       'Specific Heat': '1.188 J/g-°C',
       'Viscosity': '0.43 cP',
       'Thermal Conductivity': '0.1392 W/m-K'}

# How to define a main dictonary that nests the others
fluids_prop = {"Water" : Water,
  "Ethanol" : Ethanol,
  "Dichloromethane" : Dichloromethane
}

# How to call the entire nested dictonary
print(fluids_prop["Water"])

# How to call the nested dictonary first value
print("The density of water is,", fluids_prop["Water"]['density'])
print("The specific heat of water is,",fluids_prop["Water"]['Specific Heat'])
print("The viscosity of water is,", fluids_prop["Water"]['Viscosity'])
print("The thermal conductivity of water is,",fluids_prop["Water"]['Thermal Conductivity'])





