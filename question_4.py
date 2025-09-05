import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matrix = np.random.randint(1, 101, size=(5, 5)) #direct statement to create the desired array
sliced=matrix[1:4, 1:4] #slicing a 3*3 matrix as required
print("Original 5*5 matrix: ", matrix)
print("Extracted 3*3 matrix: ", sliced)

firstrow=sliced[0:1] #extracting first row
print("First Row: ", firstrow)

lastcolumn=sliced[:,-1] #extracting last column
print("Last Column: ", lastcolumn)

print("Dot product of the first row and last column: ", np.dot(firstrow, lastcolumn))


