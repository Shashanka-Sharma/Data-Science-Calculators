# takes in a normally distributed data set, a flag representing mean/std/correlation
# outputs the result of the flag over a window size
# Shashanka Sharma
# 08 - 12 - 21

import numpy as np
import pandas as pd
from scipy import stats

def slidWinDescStats(data, flag, subset):
    result = []
    start = 0
    end = 0
    
    while (flag != 0):
        
        new_data = data[start: end + subset]
        if (len(new_data) < subset):
            flag = 0;   
        else: 
            if flag == 1:
                result.append(int(new_data.mean()))
                    
            elif flag == 2:
                result.append(np.std(new_data))
                    
            elif flag == 3:
                if data.ndim == 2:
                    arr1 = []
                    arr2 = []
                    for i in range(len(data)):
                        arr1.append(data[i][0])
                        arr2.append(data[i][1])
                        
                    new_data1 = arr1[start: end + subset]
                    new_data2 = arr2[start: end + subset]
                    result.append(stats.pearsonr(new_data1,new_data2)[0])
    
        start += 1
        end += 1
            
        
        
    return result
    
    
    
    
    
def main():
    A = np.array([3,5,7])
    B = np.array([[1,1],[3,2],[5,4],[7,3],[9,5]])
    file = open("/Users/shashankasharma/cs_stuff/Introduction to Data Science/slidingWindowDescStatsStuff/inputArrayExample.csv")
    numpy_array = np.loadtxt(file, delimiter=",")
    #C = pd.read_csv("/Users/shashankasharma/cs_stuff/Introduction to Data Science/slidingWindowDescStatsStuff/inputArrayExample.csv")
    flag = 3
    subset = 300
    print(slidWinDescStats(numpy_array,flag,subset))  
    
main()
