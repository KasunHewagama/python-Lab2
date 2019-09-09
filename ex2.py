arr = []
for i in range (10):
    arr.append(int(input('Enter a Number : ')))
    print(arr)

def insertionSort(arr):

    for i in range (1,len(arr)): 
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
insertionSort(arr)
print('Sorted array is : ')
for i in range(len(arr)):
    print("%d" %arr[i])
