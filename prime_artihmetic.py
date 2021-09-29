import math
import random


def is_prime(num) -> bool :
    """Check wether a given number is prime or not"""

    if num == 2 :
        return True

    if num % 2 == 0 or num <= 1:
        return False

    sqrt = int(math.sqrt(num))

    for divisor in range(3, sqrt + 1, 2):
        if num % divisor == 0:
            return False
        
    return True

def gcd(a, b):
    """return the gcd of two number using Eculids algorithm"""
    if a == 0:
        return b
    else: return gcd(b % a, b)

def genRelativePrime(num, lowerBound) -> int:
    """Generate a relative prime to num by randomly choosing a number from lowerbound to max int value"""
    prim = genPrime(lowerBound, num)

    while prim % num == 0:
        prim = genPrime(lowerBound, num)

    return prim

def genPrime(lowerBound, upperBound) -> int:
    """Generate a prime number by randomly choosing a number from lowerbound to max int value"""

    primes = [x for x in range (lowerBound, upperBound) if is_prime(x)]

    return random.choice(primes)

def findMultiplicativeInverse(num1, num2):

    """Return the coffiecent for the samllest linear combination of the two(gcd)"""
    orignal = num2
    prev_s, cur_s = 1, 0
    prev_t, cur_t = 0, 1

    while num2 != 0:
        qoutient = num1 // num2
        num1, num2 = num2, num1 % num2
        prev_s, cur_s = cur_s, prev_s - qoutient * cur_s
        prev_t, cur_t = cur_t, prev_t - qoutient * cur_t
    

    return prev_s % orignal
