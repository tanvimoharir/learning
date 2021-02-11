def binarysearch(array, target, start, end):
    # recursive
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarysearch(array, target, start, mid - 1)
    elif array[mid] < target:
        return binarysearch(array, target, mid + 1, end)


def bs(array, target):
    # iterative
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            start=mid+1
        elif array[mid]>target:
            end=mid-1
    return -1
        


print(bs(array=[1, 2, 3, 4, 6, 7, 9], target=5))
