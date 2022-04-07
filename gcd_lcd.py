import numpy as np

#lcm and gcd calculator

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


def lcm(a,b):
    l = (a * b)/ gcd(a,b)
    return l


def findgcd(a,*b):
    ''' GCD of arbitrary number of numbers'''
    x = np.array([a])
    for i in b:
        x = np.append(x,i)
    xs = np.sort(x)
    while len(xs) != 1:
        xs = np.insert(xs[2:],0,gcd(xs[0],xs[1]))
    return xs[0]


def findlcm(a,*b):
    ''' LCM of arbitrary number of numbers'''
    x = np.array([a])
    for i in b:
        x = np.append(x,i)
    xs = np.sort(x)
    while len(xs) != 1:
        xs = np.insert(xs[2:],0,lcm(xs[0],xs[1]))
    return xs[0]