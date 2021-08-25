# takes in a 1D array as an input
# calculates the frequency of each unique number
# returns this data in a 2D array
# 07 - 28 - 21
# Shashanka Sharma



import numpy as np

def catCounter(arr):
    
    (unique, counts) = np.unique(arr, return_counts = True)
    frequencies = np.asarray((unique,counts)).transpose()
       
    return frequencies
    
def main():
    arr = np.array([1,2,1,2,1])
    arr2 = np.array([7,7,7,7.3,7.5])
    print(catCounter(arr))
    print("=====================")
    print(catCounter(arr2))
          
main()

