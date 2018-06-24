"""
Link: https://projecteuler.net/problem=3
Author: David Alarcón Segarra

----------------------------------------

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def largestPrimeFactor(n):     
    while n % 2 == 0:
        n = n / 2
    if n == 1:
        print(2)
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            if(i == n):
                print(i)
            n = n / i
             
largestPrimeFactor(600851475143)
