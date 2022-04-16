import random

def quicksort(arr, start, stop, comp):
    if(start < stop):
        pivotindex = partitionrand(arr,\
                            start, stop,comp)
        quicksort(arr , start , pivotindex,comp)
        quicksort(arr, pivotindex + 1, stop,comp)

def partitionrand(arr , start, stop,comp):

    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] =\
        arr[randpivot], arr[start]
    return partition(arr, start, stop,comp)

def partition(arr,start,stop,comp):   #if comp(a1,a2)  if a1 > a2 => 1, if a1 < a2 => -1, else 0
    pivot = start 
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if comp(arr[i],arr[pivot]) != -1:
                break
        while True:
            j = j - 1
            if comp(arr[j],arr[pivot]) != 1 :
                break
        if i >= j:
            return j
        arr[i] , arr[j] = arr[j] , arr[i]

def Sort(arr, comparator):
    quicksort(arr, 0, len(arr)-1, comparator)

def default_comp(a1,a2):
    if a1 > a2:
        return 1
    elif a1 < a2:
        return -1
    else:
        return 0

# if __name__ == "__main__":
#     array = [10, 7, 8, 9, 1, 5]
#     Sort(array , default_comp)
#     print(array)