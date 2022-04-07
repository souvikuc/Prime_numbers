
from divisors import total_divisors
import itertools
import math as m

def isprime(number, n_groups=20):
    '''
    Checks if a number is prime
    '''
    if number == 1 or number == 0:
        raise ValueError("Can't be determined")
    elif number == 2 or number == 3 or number == 5:
        return 1
    elif number % 2 == 0 or number % 5 == 0:
        return 0
    else:
        number_list = [i for i in range(3, m.floor(m.sqrt(number))+1) if i % 2 == 1 if i % 5 != 0]
        groups = [number_list[i:i+n_groups] for i in range(0, len(number_list), n_groups)]
        list_divisors = map(total_divisors, itertools.repeat(number), groups)
    if sum(list(list_divisors)) == 0:
        return 1
    else:
        return 0