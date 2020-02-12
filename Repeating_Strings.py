#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s_len = len(s)
    mul = n // s_len
    count = 0
    for i in s:
        if(i=='a'):
            count += 1
    count *= mul
    remain = n % s_len
    for i in range(0,remain):
        if(s[i] == 'a'):
            count += 1
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
