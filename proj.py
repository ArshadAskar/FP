#Importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path1 = '/Users/local/Downloads/suicide-mortality-borough.csv' 
file_path2 = '/Users/local/Downloads/economic-activity-by-gender.csv'
 
# Read the CSV file
smb = pd.read_csv(file_path1)
emp = pd.read_csv(file_path2)

# Filter out rows for London
smb =  smb[smb['Area name'] != 'London']
emp =  emp[emp['Area name'] != 'London']


# Display the first few rows
print(emp.head())


#Plotting
plt.plot(smb['Area name'],smb['2005'],label=('2005'))
plt.plot(smb['Area name'],smb['2009'],label=('2009'))
plt.plot(smb['Area name'],smb['2014'],label=('2014'))
plt.xticks(rotation=90)

#labelling
plt.title("Graph showing suicide rates per 100000 people in all London boroughs")
plt.xlabel("Boroughs")
plt.ylabel("Suicide rate (per 100000)")
plt.legend()
plt.show()
