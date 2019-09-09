arrl= []
for i in range (8):
    arrl.append(int(input('Enter a Number : ')))
print(arrl)

def bubbleSort(arr1):
    length = len(arrl)-1
    for i in range(length):
        for j in range(length,i,-1):
            if(arrl[j]<arrl[j-1]):
                temp = arrl[j]
                arrl[j] = arrl[j-1]
                arrl[j-1] = temp

bubbleSort(arrl)
print("Sorted Array")

for k in range(len(arrl)):
    print (arrl[k])
