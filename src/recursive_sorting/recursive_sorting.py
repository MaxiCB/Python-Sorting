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
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    arr1 = merge_sort(arr[:middle])
    arr2 = merge_sort(arr[middle:])
    print(arr1)
    print(arr2)
    return merge(arr1, arr2)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

# Timsort is implemented in python
    return sorted(arr)