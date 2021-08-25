# takes in a 2D array and power as an input
# calculates a normalized error scalar 
# returns this scalar 
# 07 - 21 - 21
# Shashanka Sharma



import numpy as np

def normalizedError(arr, power):
    
    summation = 0
    
    for i in range(len(arr)):
        summation += (abs(arr[i][0] - arr[i][1])) ** power
    
    summation /= arr.shape[0]
    
    return (summation ** (1 / power))
    
    
    
    
    
def main():
    arr = np.array([[1,2],[2,4],[3,1],[4,6],[5,2]])
    arr2 = np.array([[0,50],[10,5],[5,10]])
    power = 3
    print(normalizedError(arr2, power))
    
    
main()
