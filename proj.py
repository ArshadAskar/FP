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
smb = smb[(smb['Area name'] != 'London')]
smb = smb[(smb['Area name'] != 'Mean')]
emp = emp[(emp['Area name'] != 'London')]
emp = emp[(emp['Area name'] != 'Mean')]


# Display the first few rows
#print(emp)

#Plotting a line graph for suicide rates
#plt.plot(smb['Area name'],smb['2005'],label=('2005'),marker='o')
#plt.plot(smb['Area name'],smb['2009'],label=('2009'),marker='o')
#plt.plot(smb['Area name'],smb['2014'],label=('2014'),marker='o')
#plt.xticks(rotation=90)

#labelling
#plt.title("Graph showing suicide rates per 100000 people in all London boroughs")
#plt.xlabel("Boroughs")
#plt.ylabel("Suicide rate (per 100000)")
#plt.subplots_adjust(bottom=0.3)  # The value is a fraction of the figure height.
#plt.legend()
#plt.show()

#Plotting a line graph for economically active people
#plt.plot(emp['Area name'],emp['2005'],label=('2005'),marker='o')
#plt.plot(emp['Area name'],emp['2009'],label=('2009'),marker='o')
#plt.plot(emp['Area name'],emp['2014'],label=('2014'),marker='o')
#plt.xticks(rotation=90)

#labelling
#plt.title("Graph showing economically active people in all London boroughs")
#plt.xlabel("Boroughs")
#plt.ylabel("Number of economically active people")
#plt.subplots_adjust(bottom=0.3)  # The value is a fraction of the figure height.
#plt.legend()
#plt.show()


camden_data = emp[emp['Area name'] == 'Camden']
cam_index = camden_data.iloc[0,1:].tolist()
camden_emp = cam_index

years = np.array([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014])

#Plotting a line graph for economically active people
#plt.plot(years,camden_emp)
#plt.xticks(rotation=90)

#labelling
#plt.title("Graph showing number of economically active people in Camden")
#plt.xlabel("Borough")
#plt.ylabel("Number of economically active people")
#plt.subplots_adjust(bottom=0.3)  # The value is a fraction of the figure height.
#plt.legend()
#plt.show()

#labelling
#plt.title("Graph showing economically active people in Camden")
#plt.xlabel("Boroughs")
#plt.ylabel("Employed people")
#plt.legend()
#plt.show()

mean_suicide_df = pd.read_csv(file_path1)
mean_suicide = mean_suicide_df[mean_suicide_df['Area name'] == 'Mean']
suic_index = mean_suicide.iloc[0,1:].tolist()
meansuicide_smb = suic_index

mean_emp_df = pd.read_csv(file_path2)
mean_employment = mean_emp_df[mean_emp_df['Area name'] == 'Mean']
emp_index = mean_employment.iloc[0,1:].tolist()
meanemp_emp = emp_index


plt.plot(years,camden_emp,label='Camden')
plt.plot(years,meanemp_emp,label='London average')

#labelling
plt.title("Graph showing economically active people in Camden compared to the London average")
plt.xlabel("Time (Years)")
plt.ylabel("Number of economically active people")
plt.legend()
plt.show()
