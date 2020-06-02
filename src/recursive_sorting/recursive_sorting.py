# The merge function takes two lists and iterates n times (arrA length + arrB length)
# The merge sort function splits the given array into two arrays and recursively sorts them
# Time taken to process grows logarithmically to n
# Overal complexity: 0(nlog(n))

# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    merged_arr = []

    arrA_index = arrB_index = 0

    for _ in range(len(arrA) + len(arrB)):
        if arrA_index < len(arrA) and arrB_index < len(arrB):
            if arrA[arrA_index] <= arrB[arrB_index]:
                merged_arr.append(arrA[arrA_index])
                arrA_index += 1
            else:
                merged_arr.append(arrB[arrB_index])
                arrB_index += 1
        elif arrA_index == len(arrA):
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1
        elif arrB_index == len(arrB):
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    arr1 = merge_sort(arr[:middle])
    arr2 = merge_sort(arr[middle:])
    return merge(arr1, arr2)

    # implement an in-place merge sort algorithm
    # Need pointers for each segement
    # Compare the elements at the pointes current position
    # If p1 < p2 - p1 is correct. Increase p1
    # Else move p2
    # All elements right of p2 will be shifted right by one
    # Increase all pointers by 1

    # Seg1 is arr[1..mid]
    # Seg2 is arr[mid+1..r]
def merge_in_place(arr, start, mid, end):
    # Start point for second segment
    seg2 = mid + 1;  
    # Check if the middle and elem to the right are equal
    # If elem is less or equal then return
    if (arr[mid] <= arr[seg2]): 
        return;
    # While start < mid && seg2 less than end
    while (start <= mid and seg2 <= end):
        # if start is less than seg2 iterate start pointer
        if (arr[start] <= arr[seg2]): 
            start += 1;
        else: 
            # Copy current seg2 value
            value = arr[seg2];
            # Copy the index
            index = seg2; 
            # While the index is not start
            while (index != start): 
                # Shift all elems
                arr[index] = arr[index - 1]; 
                index -= 1; 
            # Set start element to previously saved value
            arr[start] = value; 
            # Update all pointers
            start += 1; 
            mid += 1; 
            seg2 += 1;


def merge_sort_in_place(arr, l, r): 
    if (l < r):
        # set middle
        m = l + (r - l) // 2;
        # Sort both segments of the array
        merge_sort_in_place(arr, l, m); 
        merge_sort_in_place(arr, m + 1, r); 
        # Merge both segments together
        merge_in_place(arr, l, m, r);
    # Return the sorted array
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

# Timsort is implemented in python
    return sorted(arr)