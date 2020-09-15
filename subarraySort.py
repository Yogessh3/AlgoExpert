#Time Complexity O(N) / Space Complexity O(1)
def subarraySort(array):
    minOutOfOrder=float("inf")
    maxOutOfOrder=float("-inf")
    for i in range(len(array)):
        num=array[i]
        if isOutOfOrder(i,num,array):
            minOutOfOrder=min(minOutOfOrder,num)
            maxOutOfOrder=max(maxOutOfOrder,num)
    if(minOutOfOrder==float("inf")):
        return [-1,-1]
    subarrayLeftIdx=0
    while(minOutOfOrder>=array[subarrayLeftIdx]):
        subarrayLeftIdx+=1
    subarrayRightIdx=len(array)-1
    while(maxOutOfOrder<=array[subarrayRightIdx]):
        subarrayRightIdx-=1
    return [subarrayLeftIdx,subarrayRightIdx]
def isOutOfOrder(i,num,array):
    if i==0:
        return num>array[i+1]
    elif i==len(array)-1:
        return num<array[i-1]
    return num>array[i+1] or num<array[i-1]
array=[1,2,4,7,10,11,7,12,6,7,16,18,19]
print(subarraySort(array))
        
            
