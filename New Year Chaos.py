#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(a,t):
    swaps = [0] * t

    swapped = True

    while swapped:
        swapped = False

        for i in range(t):
            if i < t - 1 and a[i] > a[i + 1]:
                swaps[a[i] - 1] += 1
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                i += 1
            print(swaps,a)    
    s = 0
    for swap in swaps:
        s += swap

        if swap > 2:
            print('Too chaotic')
            break
    else:
        print(s)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q,n)
