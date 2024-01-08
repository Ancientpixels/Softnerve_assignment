arr = [7, 10, 4, 10, 6, 5, 2]
n=len(arr)
def leader(arr,n):
    a=0
    y=0
    for i in range(n):
        if(arr[i]>=a):
            a=arr[i]
            y=i
    return y 
print(arr[leader(arr,n):])