import random 

def insertionsort(arr):
    n = len(arr)

    if n <= 1: #returns if the array only 0 or 1 element
        return
    for i in range (1, n): # starting from the second element
        key = arr[i] # store the current element in key
        j = i - 1 # initialize j to the index of the previous element
        while j >= 0 and key < arr[j]: # iterate through the sorted portion of the array
            arr[j+1] = arr[j] # shift the element to the right
            j -= 1
            arr[j+1] = key # insert the key in its correct position
    return arr

arr = []
for i in range (5):
    numbers = random.randint(1,100)
    arr.append(numbers)

print("Unordered Array: ")
print(arr)
arr = insertionsort(arr)
print("sorted Array: ")
print(arr)