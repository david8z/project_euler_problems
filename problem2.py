"""
Link: https://projecteuler.net/problem=2
Author: David Alarcón Segarra

----------------------------------------
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import itertools

def fibonacci(n):
    if(n<2):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# The fibonacci numbers that give positive results are the following
# 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48...
# I've noticed that they follow a sequence of +3 so we can use this to make it
# more efficient.

res = 0 
for i in itertools.count():
    aux = fibonacci(i*3)
    if( aux > 4000000):
        break
    else:
        res += aux

print (res)