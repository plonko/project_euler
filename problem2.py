a=[1,1]

for n in xrange(33):
    x=a[-1]
    y=a[-2]
    z=x+y
    a.append(z)
xyz=sum(o for o in a if o%2==0 and o < 4000000)
print('sum of fib numbers, with the largest being less than 4m is ' + str(xyz))