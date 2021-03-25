from matplotlib import pyplot as plt
x= [1, 2, 3, 4, 5, 6]
y=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
y1=[]
for i in y:
    print(i+1)
    y1.append(i+1)
print(y1)
#print(plt.style.available)#it shows the availabe styles


#to plot this available styles
plt.style.use("fivethirtyeight")
#plt.xkcd()#to cartoonify the plot
plt.plot(x, y, color='red', linestyle='--',linewidth=0.5, marker='o', label= 'first on line')
plt.plot(x, y1, color='blue', linestyle='--',linewidth=0.5, marker='o', label= 'second data')
plt.grid(True)
plt.xlabel("x_data")
plt.legend()
plt.tight_layout()# helps to ensure the diagram fits
plt.show()