import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#load data
#if xlsx file is chosen
#,,,,,py -3 -m pip install xlrd and py -3 -m pip install openpyxl
data = pd.read_excel('antenna.xls.xlsx')#choose either the xls or the xlsx file
#print(data.head(2))
#data column selection
theta=data.angles
power=data.power_db
# convert to radians
theta = np.deg2rad(theta)
#plot
ax = plt.subplot(111, projection='polar')
ax.plot(theta, power,color='red')
ax.set_rmax(0)
ax.set_rticks([-18,-15, -12,-9,-6,-3,0]) # less radial ticks
ax.set_rlabel_position(-22.5) # get radial labels away from plotted line
ax.grid(True)
plt.show() #display

