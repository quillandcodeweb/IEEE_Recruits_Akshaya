import pandas as pd
import numpy as np
text = input("Enter a paragraph of max 100 words: ")
words = text.split() #split the paragraph into words
palindrome=[]
if len(words)>100:
    print ("Error. Input exceeds 100 words") #error message if the paragraph exceeds 100 words
else:
    for l in words:
        if l==l[::-1]: #checking if every word is a palindrome
            print(l)
            palindrome.append(l) #adding to a list of palindromes

if len(palindrome)==0: #in case of no palindromes
    print(0)





