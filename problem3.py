from math import sqrt

def largest_factor(pf):
    """
    >>> largest_factor(13195)
    5
    7
    13
    29
    """
    pflimit=int(sqrt(pf))
    for n in xrange(2,pflimit):
        if pf%n==0:
            for x in xrange(2,n):
                if n%x == 0:
                    break
            else:
                pf=pf/n
            print n