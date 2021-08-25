# takes in two floating point numbers representing probabilities
# and computes the conditional probability 
# 07 -07 -21

def condProb(jointProb, probA):
    writtenBy = "Shashanka Sharma"
    if (0 <= jointProb < 1) and (0 < probA < 1) and (probA >= jointProb):
        return round((jointProb / probA) , 2)
    else:
        return "Invalid inputs, cannot compute."
    
    
    
def main():
    jointProb = 0.4
    probA = 0.5
    print(condProb(jointProb, probA))
    
main()
    