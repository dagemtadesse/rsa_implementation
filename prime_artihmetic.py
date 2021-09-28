import math
import sys
import random


def is_prime(num) -> bool :
    """Check wether a given number is prime or not"""

    if num == 2 :
        return True

    if num % 2 == 0 or num <= 1:
        return False

    sqrt = int(math.sqrt(num))

    for divisor in range(3, sqrt, 2):
        if num % divisor == 0:
            return False
        
    return True

def gcd(a, b):
    """return the gcd of two number using Eculids algorithm"""
    if a == 0:
        return b
    else: return gcd(b % a, b)

def genRelativePrime(lowerBound, num) -> int:
    """Generate a relative prime to num by randomly choosing a number from lowerbound to max int value"""
    prim = random.randint(lowerBound, sys.maxsize)

    while gcd(prim, num) != 1:
        prim = random.randint(num, sys.maxsize)

    return prim

def genPrime(lowerBound) -> int:
    """Generate a prime number by randomly choosing a number from lowerbound to max int value"""

    prim = random.randint(lowerBound, sys.maxsize)

    while not is_prime(genPrime):
        prim = random.randint(lowerBound, sys.maxsize)

    return prim

def findMultiplicativeInverse(num1, num2):
    pass

def euclid_algo(x, y, verbose=True):
	if x < y: # We want x >= y
		return euclid_algo(y, x, verbose)
	print()
	while y != 0:
		if verbose: print('%s = %s * %s + %s' % (x, math.floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if verbose: print('gcd is %s' % x) 
	return x


euclid_algo(150, 120)

