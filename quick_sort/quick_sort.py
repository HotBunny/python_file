# Funtion to partition the array into two halves
def partition(array, low, high):
    # Choose the pivot element (the last element in the range)
    pivot = array[high]
    # i keep track of the position of the swap element smaller than the pivot
    i = low - 1
    
    # Iterate over the array to move smaller elements before the pivot
    for j in range(low, high):
        if array[j] < pivot:
            i += 1  # Increment the index to place the next smaller element
            array[i], array[j] = array[j], array[i] # Swap the elements
            
    # Swap the pivot to its correct position (after all smaller elements)
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1 # Return the index of the pivot

# Function to sort the array using the quick sort algorithm
def quick_sort(array, low, high):
    if low < high:
        # Get the partition index (pivot position)
        pivot_index = partition(array, low, high)
        
        # Recursively sort the left and right sub-arrays
        quick_sort(array, low, pivot_index - 1) # Sort the left sub-array
        quick_sort(array, pivot_index + 1, high) # Sort the right sub-array
        
# Funtion to print the array
def print_array(array):
    print(" ".join(map(str, array)))
    
# Driver code
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print("Original array:")
    print_array(array)
    
    # Apply quick sort to the array
    quick_sort(array, 0, len(array) - 1)
    
    print("\nSorted array:")
    print_array(array)
        