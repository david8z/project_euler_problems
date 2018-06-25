"""
Link: https://projecteuler.net/problem=6
Author: David Alarcón Segarra

----------------------------------------

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
#The difference between the square of two numbers n and n+1 is equal to 2n+1 being.
import time
def method1(x):
    res = 1
    aux = 0
    for i in range(1,sum(range(x+1))):
        if (i <= x):
            aux += res 
        res = res+2*i+1
    return res-aux

def method2(x):
    aux = 0
    for i in range(1,x+1):
        aux += i**2 
    return sum(range(x+1))**2 - aux


t0 = time.time()
aux = method1(100)
t1 = time.time()
print("Method 1 in %fs, res = %f" % (t1-t0, aux ))

t0 = time.time()
aux = method2(100)
t1 = time.time()
print("Method 2 in %fs, res = %f" % (t1-t0, aux ))

