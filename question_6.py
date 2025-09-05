import pandas as pd
import numpy as np
cutoff=[("Pilani", "CS", 327), ("Goa", "CS", 301), ("Hyderabad", "CS", 298), ("Pilani", "Chemical", 247), ("Goa", "Chemical", 239), ("Hyderabad", "Chemical", 238), ("Pilani", "MSc Economics", 271), ("Goa", "MSc Economics", 263), ("Hyderabad", "MSc Economics", 261), ("Pilani", "MSc Biological Sciences", 236), ("Goa", "MSc Biological Sciences", 234), ("Hyderabad", "MSc Biological Sciences", 234),] #forming a list with the data
d={} #creating an empty dictionary
for campus, branch, score in cutoff:
    if campus not in d:
        d[campus]={}
    d[campus][branch]=score #assigning values in the required format


print("Final cutoffs of BITSAT 2024: ", d) #printing the result

