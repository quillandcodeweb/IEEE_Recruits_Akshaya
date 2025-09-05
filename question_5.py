import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

num = np.random.normal(0, 1, 1000) #generating 1000 random numbers based on normal distribution
plt.scatter(range(1000), num, alpha=0.6) #plotting the scatter plot
plt.xlabel("Index")#setting x axis label
plt.ylabel("Random Values") #setting y axis label
plt.title("Scatter Plot") #setting the title of the graph
plt.grid()
plt.show() #to display the final result

