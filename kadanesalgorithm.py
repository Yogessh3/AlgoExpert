def kadanes_algorithm(array):
    maxendReached=array[0]
    maxsoFar=array[0]
    for i in range(1,len(array)):
        maxendReached=max(array[i]+maxendReached,array[i])
        maxsoFar=max(maxsoFar,maxendReached)
    return maxsoFar
array=[2,3,6,5,4,-8,9,-4,-6,12]
print(kadanes_algorithm(array))
    
