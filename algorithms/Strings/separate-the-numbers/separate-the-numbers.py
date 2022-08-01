#!/bin/python3

import math
from operator import ne
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    if len(s) == 1:
        print("NO")
        return
    else:
        for i in range(1, len(s)//2 + 1):
            gensrt = s[:i]
            prev = int(gensrt)
            
            while len(gensrt) < len(s):
                next = prev + 1
                gensrt = gensrt + str(next)
                prev = next

            if gensrt == s:
                print("YES", s[:i])
                return

        print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
