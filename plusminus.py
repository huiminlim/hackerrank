#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    length = len(arr)

    pos = len(list(filter(lambda x: x > 0, arr)))
    zero = len(list(filter(lambda x: x == 0, arr)))
    neg = len(list(filter(lambda x: x < 0, arr)))

    pos = f"{pos/length:.6f}"
    zero = f"{zero/length:.6f}"
    neg = f"{neg/length:.6f}"
    print(pos)
    print(neg)
    print(zero)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
