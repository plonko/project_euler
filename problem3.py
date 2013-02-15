"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt
a=[]
pf=13195
pflimit=int(sqrt(pf))
for n in xrange(2,pflimit):
    if pf%n==0:
        for x in xrange(2,n):
            if n%x == 0:
                break
        else:
            pf=pf/n
        print('pf now = ' +str(n))