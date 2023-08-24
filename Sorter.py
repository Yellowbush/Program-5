# Jason Sy
# CSS 340: Applied Algorithmics
# 5/18/2022
# Sort Driver

import sort
import random
import sys

if len(sys.argv) < 2:
    print()
# BubbleSort call
elif sys.argv[1] == "bubble":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0, 9999))
            print("Pre-Sort: ", testList, "\n")
            sort.bubble_sort(testList)
            print("Post-Sort: ", testList)
    else:
        # If user did not request "PRINT"
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0, 9999))
        sort.bubble_sort(testList)
        print("LIST SORTED")
        print(testList)
# InsertionSort Call
elif sys.argv[1] == "insertion":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0, 9999))
            print("Pre-Sort: ", testList, "\n")
            sort.insertion_sort(testList)
            print("Post-Sort: ", testList)
    else:
        # If user did not request "PRINT"
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0, 9999))
        sort.insertion_sort(testList)
        print("LIST SORTED")
        print(testList)
# MergeSort Call
elif sys.argv[1] == "merge":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0, 9999))
            print("Pre-Sort: ", testList, "\n")
            sort.merge_sort(testList)
            print("Post-Sort: ", testList)
    else:
        # If user did not request "PRINT"
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0, 9999))
        sort.merge_sort(testList)
        print("LIST SORTED")
        print(testList)
# IterativeMergeSort Call
elif sys.argv[1] == "imerge":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0, 9999))
            print("Pre-Sort: ", testList, "\n")
            sort.iterative_merge_sort(testList)
            print("Post-Sort: ", testList)
    else:
        # If user did not request "PRINT"
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0, 9999))
        sort.iterative_merge_sort(testList)
        print("LIST SORTED")
        print(testList)
# QuickSort Call
elif sys.argv[1] == "quick":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0, 9999))
            print("Pre-Sort: ", testList, "\n")
            sort.quick_sort(testList)
            print("Post-Sort: ", testList)
    else:
        # If user did not request "PRINT"
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0, 9999))
        sort.quick_sort(testList)
        print("LIST SORTED")
        print(testList)
# ShellSort Call
elif sys.argv[1] == "shell":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0, 9999))
            print("Pre-Sort: ", testList, "\n")
            sort.shell_sort(testList)
            print("Post-Sort: ", testList)
    else:
        # If user did not request "PRINT"
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0, 9999))
        sort.shell_sort(testList)
        print("LIST SORTED")
        print(testList)
#Invalid Input
else:
    print("\n" + "Invalid Arguments, please use correct format.")
    print("Format required:")
    print("1) sort type as a string of characters")
    print("2) the number of integers in the list ")
    print("3) a string (PRINT) which will print the list pre-sort and post-sort. This argument is optional")
    print("Valid sort types: bubble, insertion, merge, imerge, quick, shell")