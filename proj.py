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
smb =  smb[(smb['Area name'] != 'London') & smb['Area name'] != 'Mean']
emp =  emp[(emp['Area name'] != 'London') & emp['Area name'] != 'Mean']


# Display the first few rows
print(emp.head())

#Plotting a line graph for suicide rates
#plt.plot(smb['Area name'],smb['2009'],label=('2009'))
#plt.plot(smb['Area name'],smb['2005'],label=('2005'))
#plt.plot(smb['Area name'],smb['2014'],label=('2014'))
#plt.xticks(rotation=90)

#labelling
#plt.title("Graph showing suicide rates per 100000 people in all London boroughs")
#plt.xlabel("Boroughs")
#plt.ylabel("Suicide rate (per 100000)")
#plt.legend()
#plt.show()

#Plotting a line graph for economically active people
#plt.plot(emp['Area name'],emp['2005'],label=('2005'))
#plt.plot(emp['Area name'],emp['2009'],label=('2009'))
#plt.plot(emp['Area name'],emp['2014'],label=('2014'))
#plt.xticks(rotation=90)

#labelling
#plt.title("Graph showing economically active people in all London boroughs")
#plt.xlabel("Boroughs")
#plt.ylabel("Employed people")
#plt.legend()
#plt.show()


camden_data = emp[emp['Area name'] == 'Camden']
cam_index = camden_data.iloc[0,1:].tolist()
camden_emp = cam_index

years = np.array([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014])

#Plotting a line graph for suicide rates
#plt.plot(years,camden_emp)

#plt.xticks(rotation=90)

#labelling
#plt.title("Graph showing economically active people in Camden")
#plt.xlabel("Boroughs")
#plt.ylabel("Employed people")
#plt.legend()
#plt.show()

mean_suicide = smb[smb['Area name'] == 'Mean']
suic_index = mean_suicide.iloc[0,1:].tolist()
meansuicide_emp = suic_index

mean_employment = emp[emp['Area name'] == 'Mean']
emp_index = mean_employment.iloc[0,1:].tolist()
meanemp_emp = emp_index


plt.plot(years,camden_emp,label='Camden')
plt.plot(years,meanemp_emp,label='Mean')

#labelling
plt.title("Graph showing economically active people in Camden compared to the mean")
plt.xlabel("Years")
plt.ylabel("Employed people")
plt.legend()
plt.show()
