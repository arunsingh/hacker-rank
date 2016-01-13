#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
    
primary_sum = 0
secondary_sum = 0

primary_index = 0
secondary_index = n-1

for row in a:
	primary_sum = primary_sum + row[primary_index]
	secondary_sum = secondary_sum + row[secondary_index]
	primary_index = primary_index + 1
	secondary_index = secondary_index - 1

difference = primary_sum - secondary_sum 

print(difference)  