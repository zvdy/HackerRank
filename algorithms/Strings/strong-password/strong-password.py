#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    if not any(c.islower() for c in password):
        count += 1
    if not any(c.isupper() for c in password):
        count += 1
    if not any(c.isdigit() for c in password):
        count += 1
    if not any(c.isalpha() for c in password):
        count += 1
    if len(password) < 6:
        count += 6 - len(password)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
