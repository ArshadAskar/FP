import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path = '/Users/local/Downloads/suicide-mortality-borough.csv' 

# Read the CSV file
data = pd.read_csv(file_path)

# Display the first few rows
print(data.head())

plt.xticks(rotation=90)
plt.plot(data['Area name'],data['1999'])

plt.show()