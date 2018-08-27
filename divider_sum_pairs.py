#!/bin/python

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
# Brute force
# Assumptions: list is not ordered, elements are not unique
def divisibleSumPairs(n, k, ar):
    counter = 0
    if ar.count == 0:
        return 0
    if k == 0:
        return None

    for i in range(0, n):
        for j in range(i + 1, n):
            if ((ar[i] + ar[j]) % k == 0):
                counter += 1

    return counter

if __name__ == '__main__':
    nk = raw_input().split()

    n = int(nk[0])
    k = int(nk[1])
    ar = map(int, raw_input().rstrip().split())
    result = divisibleSumPairs(n, k, ar)

    print(result)
