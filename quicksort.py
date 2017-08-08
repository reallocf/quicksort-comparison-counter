#!/usr/bin/env python
from sys import argv
from math import floor

def parse(input_list):
    with open(input_list, "r") as f:
        return(list(map(int, f.read().split('\n')[:-1])))

def first(array, low, high):
    return low

def last(array, low, high):
    return high

def median_of_three(array, low, high):
    middle = low + floor((high - low) / 2)
    if (array[high] > array[middle] and array[high] < array[low]) or (array[high] > array[low] and array[high] < array[middle]):
        return high
    elif (array[low] > array[high] and array[low] < array[middle]) or (array[low] > array[middle] and array[low] < array[high]):
        return low
    else:
        return middle

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def partition(pivot_selector, array, count, low, high):
    i = low
    pivotIndex = pivot_selector(array, low, high)
    pivot = array[pivotIndex]
    swap(array, low, pivotIndex)
    count[0] += high - low
    for j in range(low + 1, high + 1):
        if (array[j] < pivot):
            i += 1
            swap(array, i, j)
    swap(array, i, low)
    return i

def quicksort(pivot_selector, array, count, low, high):
    if (low < high):
        pivotIndex = partition(pivot_selector, array, count, low, high)
        quicksort(pivot_selector, array, count, low, pivotIndex - 1)
        quicksort(pivot_selector, array, count, pivotIndex + 1, high)
    return array

if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: ./quicksort.py newline-divided-list")
        exit()
    parsedList1 = parse(argv[1])
    parsedList2 = list(parsedList1)
    parsedList3 = list(parsedList1)
    count1 = [0]
    count2 = [0]
    count3 = [0]
    print("FIRST: " + str(quicksort(first, parsedList1, count1, 0, len(parsedList1) - 1)))
    print("COUNT: " + str(count1[0]))
    print("LAST: " + str(quicksort(last, parsedList2, count2, 0, len(parsedList2) - 1)))
    print("COUNT: " + str(count2[0]))
    print("MEDIAN OF THREE: " + str(quicksort(median_of_three, parsedList3, count3, 0, len(parsedList3) - 1)))
    print("COUNT: " + str(count3[0]))
