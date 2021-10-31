arr=[5,4,3,2,1]
length = len(arr)
print("orignal array is %d",arr)
for i in range(0,length):
    for j in range(0,length-1):
        if(arr[j] > arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
print("Sorted array is %d ",arr)
