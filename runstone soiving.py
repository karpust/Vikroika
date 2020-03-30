"""3.3 Self Check
Write two Python functions to find the minimum number in a list.
The first function should compare each number to every other number on the list. O(n**2).
The second function should be linear O(n).
"""
import time
from random import randrange


# print(ls)
ls = [3, 2, 5, 6, 9, 7, 4, 1]


# def timeit(func):
#     def wraper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         print("size: %d time: %f" % (listsize, end - start))
#         return result
#     return wraper


# @timeit
def square(l):
    mini = 0
    for i in l:
        for j in l:
            if j < i:
                mini = j
        # print(i)
    return mini


# @timeit
def lin(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    # print(min)
    return min


# timeit(square)(ls)
# lin(ls)

# for listsize in range(0, 10001, 2000):
#     ls = [randrange(10000)for x in range(listsize)]
#     start = time.time()
#     square(ls)
#     end = time.time()
#     print("size: %d time: %f" % (listsize, end - start))


for listsize in range(0, 10001, 2000):
    ls = [randrange(10000)for x in range(listsize)]
    start = time.time()
    lin(ls)
    end = time.time()
    print("size: %d time: %f" % (listsize, end - start))