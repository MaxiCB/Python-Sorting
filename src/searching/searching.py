# STRETCH: implement Linear Search				
def linear_search(arr, target):
    min_val = 0
    max_val = len(arr)

    for i in range(min_val, max_val):
        if len(arr) == 0:
            return -1
        if arr[i] == target:
            return i
        elif arr[i] > target:
            max_val = i
        elif arr[i] < target:
            min_val = i

    # Return not found
    return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    low = 1
    high = len(arr)

    found = False

    while low <= high:
        if high < low:
            return -1

        middle = low + (high - 1) // 2

        if arr[middle] == target:
            print('Found middle', middle)
            return middle

        elif arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
  # The array received was a empty array. Return -1
  if high >= low:

    if len(arr) == 0:
      return -1

    middle = (low + high) // 2

    if arr[middle] == target:
        print(middle)
        return middle

    elif arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle - 1)
    else:
      return binary_search_recursive(arr, target,middle + 1, high)
  else:
    return -1