# code adapted from https://www.educative.io/edpresso/merge-sort-in-python
def mergesort(array):
    # function which recursively splits an array which is required for merge sort implementation
    if len(array) > 1:
        mid = len(array) // 2
        left = array[mid:]
        right = array[:mid]

        mergesort(left)
        mergesort(right)

        # initializing the iterators
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # to make sure that the left and right halves are traversed entirely
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


array = [3, 6, 4, 1, 7]
mergesort(array)
print(array)
