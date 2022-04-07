
from getprime import getprime
from isPrime import isprime

def getprime(a,n):
    '''
    Finds n-th primes starting from a . If a is prime it will count a as first prime
    '''
    if a == 1 or a == 0:
        return getprime(2,n)
    else:
        s = 0
        while s < n:
            if isprime(a):
                s = s + 1
                prime = a
                a = a + 1
            else:
                a = a + 1
        return prime