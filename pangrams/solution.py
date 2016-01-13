#!/bin/python3

#pangrams
#s = 'We promptly judged antique ivory buckles for the next prize'
#s = 'We promptly judgEd antique ivory buckles for the next prize'

#not pangram
#s = 'We promptly judged antique ivory buckles for the prize'

s = input().strip().lower()

"""
The english alphabet has 26 letters, so
if after the elimination of duplicate characters
in the string the character count was less then 26 
it means that is not a pangram.

Consider that a string might contain uppercase and 
lowercase letters.

IMPORTANT: The order here does not matter. If the order 
does matter the complexity might increase.
"""

clean_sentence = ''.join(set(s))

if (len(clean_sentence)-1) == 26:
	print('pangram')
else:
	print('not pangram')
