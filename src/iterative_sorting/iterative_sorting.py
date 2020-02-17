# TO-DO: Implement the Selection Sort function below 
def selection_sort(arr):
    # Loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i

        # Starting from the right of the current index do a loop
        for j in range(i + 1, len(arr)):
            # If j is less than current index set j to current index
            if arr[j] < arr[cur_index]:
                cur_index = j
        # Swap cur_index and i elements
        arr[cur_index], arr[i] = arr[i], arr[cur_index]
        print(cur_index)
    # Return the array once completed
    print(arr)
    return arr


# TO-DO:  Implement the Bubble Sort function below
def bubble_sort( arr ):
    # Loop through the array n-1 elements
    for i in range(0, len(arr) - 1):
        # Set swapped flag to false for future break
        swapped = False
        # Loop through array n-1 elements as j
        for j in range(0, len(arr) - 1):
            # Check if j is greater than j+1 element
            if arr[j] > arr[j + 1]:
                # Set swapped flag to eliminate break
                swapped = True
                # Swap j, j + 1 elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # If nothing was swapped in the loop break out
        if swapped == False:
            break
    print(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        if arr[i] < 0:
            return 'Error, negative numbers not allowed in Count Sort'
    for i in range(0, size):
        count[arr[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(0, size):
        arr[i] = output[i]
    print(arr)
    return arr