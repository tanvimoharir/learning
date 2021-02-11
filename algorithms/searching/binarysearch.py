
def binarysearch(array,target,start,end):
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binarysearch(array,target,start,mid-1)
    elif array[mid]<target:
        return binarysearch(array,target,mid+1,end)


print(binarysearch(array=[1,2,3,4,6,7,9],target=2,start=0,end=6))