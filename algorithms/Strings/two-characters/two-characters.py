#!/bin/python3

import math
import os
import random
import re
import sys

# had to import this
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    m = 0
    # imported combinations from itertools for this problem
    for i in (combinations(set(s),2)):
        j = "".join(i)
        t = re.sub("[^%s]"%j, "",s)
        if len(t)>m and not re.search(r"(\w)\1", t) :
            m = len(t)
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
