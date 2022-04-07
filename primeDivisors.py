import numpy as np
from findPrimes import findprimes
from isPrime import isprime
from get_exponent import getexponent
import numbers



def primedivisors(n):
    '''
    Finds the prime divisors along with their number of occurences (power)
    '''
    if n == 0 or n == 1:
        return None
    elif isprime(n):
        s = [(n, 1)]
        return np.array(s)
    else:
        primes = findprimes(1, n//2)
        s = []
        while n != 1:
            for i in primes:
                if n % i == 0:
                    x = getexponent(n, i)
                    s.append((i, x))
                    n = n/(i**x)
        return np.array(s)