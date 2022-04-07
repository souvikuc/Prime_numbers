# Finds the maximum exponent of a that divides n

import numbers


def getexponent(n,a):
    if a == 1 or a == 0:
        raise ValueError("a can't be {}".format(a))
    if isinstance(n,numbers.Number) and isinstance(a,numbers.Number):
        s = 0
        while n % a == 0:
            s = s + 1
            n = n / a
            getexponent(n,a)
        return s
    elif isinstance(n,numbers.Number)==False:
        raise ValueError(f"{n} is not a digit")
    else:
        raise ValueError(f"{a} is not a digit")