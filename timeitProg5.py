
import timeit
from sort import data_size


bubble_SetupCode = '''
import random
import sort
from random import randint
from sort import data_size
testList = []
for i in range(data_size):
    testList.append(random.randint(0, 1000))
'''
bubble_TestCode = '''
sort.bubble_sort(testList)
'''


insertion_SetupCode = '''
import random
import sort
from random import randint
from sort import data_size
testList = []
for i in range(data_size):
    testList.append(random.randint(0, 1000))
'''
insertion_TestCode = '''
sort.insertion_sort(testList)
'''


merge_SetupCode = '''
import random
import sort
from random import randint
from sort import data_size
testList = []
for i in range(data_size):
    testList.append(random.randint(0, 1000))
'''
merge_TestCode = '''
sort.merge_sort(testList)
'''


imerge_SetupCode = '''
import random
import sort
from random import randint
from sort import data_size
testList = []
for i in range(data_size):
    testList.append(random.randint(0, 1000))
'''
imerge_TestCode = '''
sort.iterative_merge_sort(testList)
'''


quick_SetupCode = '''
import random
import sort
from random import randint
from sort import data_size
testList = []
for i in range(data_size):
    testList.append(random.randint(0, 1000))
'''
quick_TestCode = '''
sort.quick_sort(testList)
'''


shell_SetupCode = '''
import random
import sort
from random import randint
from sort import data_size
testList = []
for i in range(data_size):
    testList.append(random.randint(0, 1000))
'''
shell_TestCode = '''
sort.shell_sort(testList)
'''


bubble = timeit.timeit(setup = bubble_SetupCode, stmt=bubble_TestCode, number = 1)
insertion = timeit.timeit(setup = insertion_SetupCode, stmt=insertion_TestCode, number = 1)
merge = timeit.timeit(setup = merge_SetupCode, stmt=merge_TestCode, number = 1)
imerge = timeit.timeit(setup = imerge_SetupCode, stmt=imerge_TestCode, number = 1)
quick = timeit.timeit(setup = quick_SetupCode, stmt=quick_TestCode, number = 1)
shell = timeit.timeit(setup = shell_SetupCode, stmt=shell_TestCode, number = 1)

print("Bubble   ", data_size, " :   {}".format(bubble))
print("Insertion", data_size, " :   {}".format(insertion))
print("Merge    ", data_size, " :   {}".format(merge))
print("iMerge   ", data_size, " :   {}".format(imerge))
print("Quick    ", data_size, " :   {}".format(quick))
print("Shell    ", data_size, " :   {}".format(shell))