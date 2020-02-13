import unittest
import random
from src.recursive_sorting.recursive_sorting import *

class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        # This is for testing the merge functionality I implemented
        self.assertEqual(merge(arr3, arr3), [2,2])
        self.assertEqual(merge(arr4, arr3), [0, 1, 2, 2, 3, 4, 5])
        # Testing of the actual merge sort functionality
        self.assertEqual(merge_sort(arr1), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(merge_sort(arr2), [])
        self.assertEqual(merge_sort(arr3), [2])
        self.assertEqual(merge_sort(arr4), [0,1,2,3,4,5])
        self.assertEqual(merge_sort(arr5), sorted(arr5))

        self.assertEqual(timsort(arr5), sorted(arr5))


if __name__ == '__main__':
    unittest.main()