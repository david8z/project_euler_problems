"""
Link: https://projecteuler.net/problem=4
Author: David Alarcón Segarra

----------------------------------------


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#Basically the problem is telling us to do the LCM of all the numbers form 1 to 20

def gcd(a, b):
    d = 0
    while a % 2 == 0 and b % 2 == 0:
        a = a/2
        b = b/2
        d += 1
    while (a != b):
        if a % 2 == 0:
            a = a/2
        elif b % 2 == 0:
            b = b / 2
        elif a > b:
            a = (a - b) / 2
        else:
            b = (b - a) / 2

    return a * 2 ** d

def lcm(a, b):
    return (a*b)/gcd(a,b)

res = 1
for i in range(1,20):
    res = lcm(res, i)

print(res)

    
    
