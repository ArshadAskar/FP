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
print(emp)

#Plotting a line graph for suicide rates
plt.plot(smb['Area name'],smb['2005'],label=('2005'),marker='o')
plt.plot(smb['Area name'],smb['2009'],label=('2009'),marker='o')
plt.plot(smb['Area name'],smb['2014'],label=('2014'),marker='o')
plt.xticks(rotation=90)

#labelling
plt.title("Graph showing suicide rates per 100000 people in all London boroughs")
plt.xlabel("Boroughs")
plt.ylabel("Suicide rate (per 100000)")
plt.subplots_adjust(bottom=0.3)  # The value is a fraction of the figure height.
plt.legend()
plt.show()

#Plotting a line graph for economically active people
plt.plot(emp['Area name'],emp['2005'],label=('2005'),marker='o')
plt.plot(emp['Area name'],emp['2009'],label=('2009'),marker='o')
plt.plot(emp['Area name'],emp['2014'],label=('2014'),marker='o')
plt.xticks(rotation=90)

#labelling
plt.title("Graph showing economically active people in all London boroughs")
plt.xlabel("Boroughs")
plt.ylabel("Number of economically active people")
plt.subplots_adjust(bottom=0.3)  # The value is a fraction of the figure height.
plt.legend()
plt.show()

# Getting the data into a list
camden_data = emp[emp['Area name'] == 'Camden']
cam_index = camden_data.iloc[0,1:].tolist()
camden_emp = cam_index

islington_data = emp[emp['Area name'] == 'Islington']
isl_index = islington_data.iloc[0,1:].tolist()
islington_emp = isl_index

westminster_data = emp[emp['Area name'] == 'Westminster']
west_index = westminster_data.iloc[0,1:].tolist()
westminster_emp = west_index

Southwark_data = emp[emp['Area name'] == 'Southwark']
south_index = Southwark_data.iloc[0,1:].tolist()
Southwark_emp = south_index

years = np.array([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014])

camden_suicide_data = smb[smb['Area name'] == 'Camden']
camden_index = camden_suicide_data.iloc[0,1:].tolist()
camden_smb = camden_index

islington_suicide_data = smb[smb['Area name'] == 'Islington']
isling_index = islington_suicide_data.iloc[0,1:].tolist()
islington_smb = isling_index

westminster_suicide_data = smb[smb['Area name'] == 'Westminster']
westmins_index = westminster_suicide_data.iloc[0,1:].tolist()
westminster_smb = westmins_index

southwark_suicide_data = smb[smb['Area name'] == 'Southwark']
southwa_index = southwark_suicide_data.iloc[0,1:].tolist()
southwark_smb = southwa_index

#Plotting a line graph for economically active people
plt.plot(years,camden_emp)
plt.xticks(rotation=90)

#labelling
plt.title("Graph showing number of economically active people in Camden")
plt.xlabel("Borough")
plt.ylabel("Number of economically active people")
plt.subplots_adjust(bottom=0.3)  # The value is a fraction of the figure height.
plt.legend()
plt.show()

# Getting the data into a list
mean_suicide_df = pd.read_csv(file_path1)
mean_suicide = mean_suicide_df[mean_suicide_df['Area name'] == 'Mean']
suic_index = mean_suicide.iloc[0,1:].tolist()
meansuicide_smb = suic_index

mean_emp_df = pd.read_csv(file_path2)
mean_employment = mean_emp_df[mean_emp_df['Area name'] == 'Mean']
emp_index = mean_employment.iloc[0,1:].tolist()
meanemp_emp = emp_index

#Plotting camden economically active and london average
plt.plot(years,camden_emp,label='Camden',marker='o')
plt.plot(years,meanemp_emp,label='London average',marker='o')

#labelling
plt.title("Graph showing economically active people in Camden compared to the London average")
plt.xlabel("Time (Years)")
plt.ylabel("Number of economically active people")
plt.legend()
plt.show()

# Plotting HSB
plt.plot(years,islington_emp,label='Islington',marker='o')
plt.plot(years,westminster_emp,label='Westminster',marker='o')
plt.plot(years,Southwark_emp,label='Southwark',marker='o')
plt.plot(years,meanemp_emp,label='London average',marker='o')

#labelling
plt.title("Graph showing economically active people in high suicide rate boroughs compared to the London average")
plt.xlabel("Time (Years)")
plt.ylabel("Number of economically active people")
plt.legend()
plt.show()


# Mean for high suicide boroughs
Mean_high_suicide1 = []
Mean_high_suicide2 = []
Mean_high_suicide1 = np.array(camden_emp) + np.array(islington_emp) + np.array(westminster_emp) + np.array(Southwark_emp)
for i in range(len(Mean_high_suicide1)):
    val = round(Mean_high_suicide1[i]/ 4)
    Mean_high_suicide2 = np.append(Mean_high_suicide2,val)

Mean_high_suicide3 = []
Mean_high_suicide4 = []
Mean_high_suicide3 = np.array(camden_smb) + np.array(islington_smb) + np.array(westminster_smb) + np.array(southwark_smb)
for i in range(len(Mean_high_suicide3)):
    val = round(Mean_high_suicide3[i]/ 4)
    Mean_high_suicide4 = np.append(Mean_high_suicide4,val)


# Graph for HSB suicide rates and HSB economically active population
fig,ax1 = plt.subplots()
qual1,= ax1.plot(years,Mean_high_suicide4,marker='o',color = 'blue',label=("Suicide average"))
ax2 = ax1.twinx()
qual2, = ax2.plot(years,Mean_high_suicide2,marker='o',color ='red',label=("Economically active average"))
plt.xticks(years,rotation = "vertical")

# Labelling
plt.title("Graph showing high suicide boroughs suicide rates (per 100,000) and their economically active population")
ax1.set_xlabel("Time (Years)")
ax1.set_ylabel('Suicide average (per 100,000)')
ax2.set_ylabel("Economically active average")
ax1.legend(handles=[qual1, qual2])
plt.show()

# Headline figure - comparing average london suicide and average economically active population    
fig,ax1 = plt.subplots()
qual3,= ax1.plot(years,meansuicide_smb,marker='o',color = 'black',label=("Suicide average"),linestyle='--')
ax2 = ax1.twinx()
qual4, = ax2.plot(years,meanemp_emp,marker='x',color ='red',label=("Economically active average"),linestyle='--')
plt.xticks(years,rotation = "vertical")
ax1.grid(True, which='both', linestyle='-.', linewidth=0.5, alpha=0.5)


# Labelling
plt.title("Graph showing London average suicide rates (per 100,000) and their average economically active population")
ax1.set_xlabel("Time (Years)")
ax1.set_ylabel('Suicide average (per 100,000)')
ax2.set_ylabel("Economically active average")
ax1.legend(handles=[qual3, qual4])
ax1.text(2006,10.7, 'Correlation coefficient = - 0.91', fontsize=12, color='black', style='italic')
plt.show()
corr = np.corrcoef(meanemp_emp,meansuicide_smb)[0,1]
print(corr)

