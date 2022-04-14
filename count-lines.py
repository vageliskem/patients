"""
This script counts the number of files in standard input.
Input: strings from the system's standard input
"""


import sys 

count=0

for line in sys.stdin:
	count +=1

print(count, 'lines in standard input')
