#Dalton Price
# 1/28/23
# Reads file about states with most platinum hits, then creates and displays bar graph

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('pltalbums.csv')
print(df[['City', 'Total Albums']])

#Set x and y values from df info
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

#create plt
fig, ax = plt.subplots()

#creat bar graph an set which values to use from df
ax.bar(df['City'], df['Total Albums'])
plt.xticks(rotation=90)

#set bar graph labels
plt.xlabel('City')
plt.ylabel('Total Number')

#display graph
plt.show()

