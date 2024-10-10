def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        swapped = False  # Flag to check if a swap was made
        # Last i elements are already sorted, no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set flag to True if a swap occurs

        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array: ", arr)
    bubble_sort(arr)
    print("Sorted array: ", arr)
