import matplotlib.pyplot as plt

# line 1 points
x1 = [20,30,40,50,60,70,80,90,100]
y1 = [12.5,9.87,10.68,13.06,25.18,29.09,35.32,32.34,32.51]
# plotting the line 1 points
plt.plot(x1, y1, label = "RMS algorithm")

# line 2 points
x2 = [20,30,40,50,60,70,80,90,100]
y2 = [11.75,9.00,10.68,12.98,15.73,20.7,28.74,26.14,27.68]
# plotting the line 2 points
plt.plot(x2, y2, label = "EDF algorithm")

# naming the x axis
plt.xlabel('No of processes')
# naming the y axis
plt.ylabel('No of deadline missed')
# giving a title to my graph


# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
