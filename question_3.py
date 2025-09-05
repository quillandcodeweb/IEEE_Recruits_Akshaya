#Create a 5x5 numpy matrix with random integers between 1 and 100. Print it in a grid format, along with the maximum, minimum and mean of the numbers. Normalise the value of elements between 0-1. Flatten the matrix to a 1D array, sort it and print it.
import pandas as pd
import numpy as np
matrix = np.random.randint(1, 101, size=(5, 5)) #direct statement to create the desired array
print("Original 5x5 Matrix: ", matrix) #printing the matrix as asked
maxx = np.max(matrix) #maximum value
minn = np.min(matrix) #minimum value
meann = np.mean(matrix) #mean value

print("Maximum value: ", maxx)
print("Minimum value: ", minn)
print("Mean: ", meann) #printing the max, min, mean as required

normalized = (matrix - minn) / (maxx - minn) #normalizing the array
print("Normalized Matrix: ", normalized)

flat = matrix.flatten()
sortflat = np.sort(flat) #sorting the values
print("Flattened and Sorted Array: ", sortflat) #printing the final flattened and sorted array