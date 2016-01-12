#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

current_sum = 0
MAX_INT = 2147483647
MIN_INT = -2147483648

for x in arr:
    min_possible_value = MIN_INT + x
    max_possible_value = MAX_INT - x
    
    if x >= min_possible_value <= max_possible_value:
        current_sum = current_sum + x
    else:
        pass
    
print(current_sum)