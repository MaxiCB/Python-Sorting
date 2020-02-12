# TO-DO: Implement the Selection Sort function below 
def selection_sort( arr ):
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
    # Return the arrray once completed
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
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr