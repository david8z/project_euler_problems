"""
Link: https://projecteuler.net/problem=7
Author: David Alarcón Segarra

----------------------------------------

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

primes = [2]
i = 3
aux = 0 
while len(primes) < 10001:
    for p in primes:
        if i % p == 0:
            break;
        else:
            aux+=1
        
    if aux == len(primes):
        primes.append(i)
    aux = 0
    i += 1

print(primes[-1])
