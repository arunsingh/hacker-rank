#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

""" Simply reverse the list items """
arr.reverse()

""" 
print them inline by joinning items separeted 
with a single space 
"""
print(" ".join([str(x) for x in arr] ))