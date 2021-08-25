# Takes in a 1D array as a parameter then calculates the Mean
# Absolute Deviation by finding the the median of the deviations 
# from the median.
# 07 - 14 - 21 

import numpy as np


def medAbsDev(array):
    writtenBy = "Shashanka Sharma"
    median = np.median(array)
    
    for i in range(len(array)):
        array[i] = median - array[i]
    
    return np.median(abs(array))
        
  
def main():
    alpha = np.array([4.5,3.2,1.5,5.7,9.3,2.2,6.9])
    print(medAbsDev(alpha))
    
main()