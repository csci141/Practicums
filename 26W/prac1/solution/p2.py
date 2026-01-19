# Author:
# Date:
# Practicum 1, Problem 2

""" This program prints an integer subtraction problem with the numbers
nicely aligned. The program takes two integers, a and b, as command line
arguments. Both x and y are positive, and x is assumed to be larger than y, so
that their difference is positive. The program prints three lines:
- x with one leading space.
- a minus sign, then the y with enough leading spaces to line its digits up
  with the corresponding digits of the first number
- an equals sign then x-y, similarly padded to align with the first two

Example runs:
>>> %Run p3.py 5 4
 5
-4
=1
>>> %Run p3.py 53 4
 53
- 4
=49
>>> %Run p3.py 100 99
 100
- 99
=  1

Helpful Tip: recall the len function from lab 1. 
"""

import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

len1 = len(str(n1))
len2 = len(str(n2))
len3 = len(str(n1-n2))

pad1 = (len1 - len2) * " "
pad2 = (len1 - len3) * " "

print(" ", n1, sep="")
print("-", pad1, n2, sep="")
print("=", pad2, n1 - n2, sep="")
