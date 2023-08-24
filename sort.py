# Jason Sy
# CSS 340: Applied Algorithmics
# 5/18/2022
# Six types of sorting method

data_size = 500

# bubble sort
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) -  i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

# insertion sort
def insertion_sort(list):
    for place in range(1, len(list)):
        temp = list[place]
        i = place
        while i > 0 and list[i - 1] > temp:
            list[i] = list[i - 1]
            i -= 1
        list[i] = temp

# MergeSort recursive
def merge_sort(list):
    if len(list) >  1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

# Iterative MergeSort function
def iterative_merge_sort(list):
    size = 1
    length = len(list)
    while size < length:
        left = 0
        while (left < length):
            right = min(left + (size * 2 - 1), length - 1)
            mid = min(left + size - 1, length - 1)
            merge(list, left, mid, right)
            left += size*2
        size *= 2
    return list

# merge function   
def merge(list, left, mid, right):
    first = mid - left + 1
    last = right - mid
    left1 = [0] *  first
    right1 = [0] * last
    for i in range(0, first):
        left1[i] = list[left + i]
    for i in range(0, last):
        right1[i] = list[mid + i + 1]
    i = 0
    j = 0
    k = left
    while i < first and j < last:
        if left1[i] <= right1[j]:
            list[k] = left1[i]
            i += 1
        else:
            list[k] = right1[j]
            j += 1
        k += 1
    while i < first:
        list[k] = left1[i]
        i += 1
        k += 1
    while j < last:
        list[k] = right1[j]
        j += 1
        k += 1

# quick sort worker
def quick_sort_worker(list, first, last):
    if len(list) == 1:
        return list
    if first < last:
        index = partition(list, first, last)
        quick_sort_worker(list, first, index - 1)
        quick_sort_worker(list, index + 1, last)

# quick sort
def quick_sort(list):
    quick_sort_worker(list, 0, len(list) - 1)
    return list

# partition function
def partition(list, first, last):
    i = (first - 1)
    pivot = list[last]
    for j in range(first, last):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[last] = list[last], list[i + 1]
    return (i + 1)

#shell sort
def shell_sort(list):
    size = len(list)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = list[i]
            j = i
            while j >= gap and temp < list[j - gap]:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        if gap == 2:
            gap = 1
        else:
            gap = int(gap / 2.2)
