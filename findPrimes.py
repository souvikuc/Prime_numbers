import math as m
from isPrime import isprime



def findprimes(a,b):
    '''
    Find prime numbers between (a,b) or (b,a) 
    '''
    
    l = []
    if a <= b:
        for i in range(m.ceil(a)+1,m.floor(b)+1):
            if isprime(i):
                l.append(i)
    else:
        findprimes(b,a)
    return l





#Another way to write the same program


def findprimes1(a,b):
    if a <= b:
        l =list(filter(isprime,range(m.ceil(a)+1,m.floor(b)+1)))
    else:
        return findprimes1(b,a)
    return l