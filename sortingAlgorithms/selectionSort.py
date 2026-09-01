import random

def selectionSort(arr):
    size = len(arr) #Takes the size of the array
    for i in range (size - 1): #iterates through the outer array
        min_index = i #assumes i is the min index
        for j in range(i + 1, size): #iterates the next element to the selected j element
            if arr[j] < arr[min_index]: #Determines if the j element is less than min index 
                min_index = j #initializes min index to j
        arr[min_index], arr[i] = arr[i], arr[min_index] #swaps i with the min index
    return arr


arr = []
for i in range (5):
    num = random.randint(1, 100)
    arr.append(num)

print("Original array:")
print(arr)
arr = selectionSort(arr)
print("Sorted array through selection sort: ")
print(arr)