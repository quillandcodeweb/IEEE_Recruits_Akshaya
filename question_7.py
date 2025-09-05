import pandas as pd
import numpy as np
L1=[1, 43, 56, 35, 37, 9, 46, 35]
L2=[35, 82, 47, 46, 18, 1, 80, 100, 35] #two random lists
L=[] # a list to store the common elements
for a in range(0, len(L1)):
    if L1[a] in L2: #checking the existence of every individual element in the second list
        if L1[a] not in L: #checking to avoid duplicates in the final list
            L.append(L1[a]) #adding the common element (if any) to the list


print("The list of common elements in both the lists: ", L) #printing the final list of common elements