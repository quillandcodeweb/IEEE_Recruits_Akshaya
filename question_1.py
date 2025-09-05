import pandas as pd
n=int(input("Enter a number n for the number of rows: ")) #asking the user for input
for a in range (1, n+1):
    for b in range (1, n+1-a): #inner loop for the number of spaces, descending
        print(" ", end="")
    for c in range (1, a+1): #inner loop for the number of asterix signs, ascending
        print("*", end="")
    print() #ending every line

