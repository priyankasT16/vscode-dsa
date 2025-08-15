def Bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(0,n):
        key = arr[i]
        j = i-1
        while j>= 0 and key<arr[j+1]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
    return arr

arr = [10,6,3,7]
sorted_arr = Bubble_sort(arr)
print(sorted_arr)

