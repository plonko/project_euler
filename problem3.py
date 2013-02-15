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