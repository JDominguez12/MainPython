import random

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break
    return arr

arr = []
for i in range (5):
    randomVal = random.randint(1, 1000)
    arr.append(randomVal)

print("Original array: ")
print(arr)
arr2 = bubblesort(arr)
arr.sort()
print("Sorted array using the sort function: ")
print(arr)
print("Sorted array using the Bubblesort function: ")
print(arr2)



