# takes in a distribution and value between float between 0 and 100
# computes the upper and lower bounds (tails)
# outputs the data's lower and upper bounds given the bound.
# Shashanka Sharma
# 08 - 04 - 21

import numpy as np
import pandas as pd


def empiricalSampleBounds(input_data, bound):
 
    length = len(input_data)
    data = input_data.sort_values(by = 0)
     
    probability_mass = (100 - bound) / 200
 
    bound_index = int(round(probability_mass * length))  
    
    return (data.iloc[bound_index - 1], data.iloc[-bound_index - 1])
    
    

def main():
    
    input_data = np.array([1,2,3,4,5,6,7,8,9,10])
    input_data2 = pd.read_csv("/Users/shashankasharma/Downloads/sampleInput1.csv", header = None)
    input_data3 = pd.read_csv("/Users/shashankasharma/Downloads/sampleInput2.csv", header = None)
    bound = 99
    result = empiricalSampleBounds(input_data3, bound)
    print("lower bound: " , result[0],)
    print("upper bound: " , result[1])
    
    
    
main()
    
    