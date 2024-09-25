from typing import List

def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    # Copy the sub-arrays for merging
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Merge back into arr
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy any remaining elements
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        mid = (left + right) // 2
        
        # Recursively sort the two halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Merge sorted halves
        merge(arr, left, mid, right)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    
    print('Given array is:', arr)
    
    if arr:
        merge_sort(arr, 0, len(arr) - 1)
    
    print('Sorted array is:', arr)
