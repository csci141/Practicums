# Author:
# Date: 
# Practicum 1, Problem 1

""" This program calculates the difference between two fractions. For example,
1/2 and 3/4 are a distance of 0.25 apart.

The program takes four command line arguments.
- The first two arguments are the integer numerator and denominator of the
  first fraction
- The next two arguments are the integer numerator and denominator of the
  second fraction.

The program outputs three lines.
- The first two lines print the fraction and decimal representation of the
  first and second fractions, respectively.
- The third line prints the difference between the two fractions as a decimal.
See the example runs for the specific formatting of the output:

>>> %Run p1.py 1 2 3 4
1 / 2 is 0.5
3 / 4 is 0.75
Their difference is 0.25
>>> %Run p1.py 5 4 3 2
5 / 4 is 1.25
3 / 2 is 1.5
Their difference is 0.25
"""

import sys

n1 = int(sys.argv[1])
d1 = int(sys.argv[2])
f1 = n1/d1

n2 = int(sys.argv[3])
d2 = int(sys.argv[4])
f2 = n2/d2

print(n1, "/", d1, "is", f1)
print(n2, "/", d2, "is", f2)


print("Their difference is", n2/d2 - n1/d1)