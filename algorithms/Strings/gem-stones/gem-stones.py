#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Write your code here
    # gem stones hackerrank
    #
#There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in the collection.
#Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.
    if len(arr) == 1:
        return len(arr[0])
    else:
        gems = set(arr[0])
        for i in range(1, len(arr)):
            gems = gems.intersection(set(arr[i]))
        return len(gems)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
