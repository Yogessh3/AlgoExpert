def swap(i,j,array):
    array[i],array[j]=array[j],array[i]
    return array
def bubbleSort(array):
    isSorted=False
    counter=0
    while not isSorted:
        isSorted=True
        for i in range(len(array)-1-counter):
            if(array[i]>array[i+1]):
                swap(i,i+1,array)
                isSorted=False
        counter+=1
    return array
array=[8,5,3,2,1,0]
v=bubbleSort(array)
print(v)
