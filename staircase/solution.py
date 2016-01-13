#!/bin/python3

import sys

n = int(input().strip())

"""
Desired output for an input height of 6

     #
    ##
   ###
  ####
 #####
######

n-1 spaces at the top
0 spaces at the bottom

"""

spaces = n-1

for x in range(0, n):
	space_string = ' ' * spaces
	hash_string = '#' * (n-spaces)
	print(space_string + hash_string)
	spaces -= 1