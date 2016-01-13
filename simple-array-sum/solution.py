#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr_sum = 0

for n in arr:
  arr_sum = arr_sum + n

print(arr_sum)
