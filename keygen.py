import math
import sys


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


p = 1009
q = 2741

if not is_prime(p):
    raise ValueError('P is not prime')
if not is_prime(q):
    raise ValueError('Q is not prime')

x = 1

eq = (p - 1) * (q - 1) + 1

y = 1
xy = x*y

while xy != eq:
    x += 1
    y = eq / x
    xy = x*y


print ("public key, x: " + str(x))
print ("private key, y: " + str(y))
print ("modulo (pq): " + str(p*q))