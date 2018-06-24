"""
Link: https://projecteuler.net/problem=4
Author: David Alarcón Segarra

----------------------------------------
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPalindrome(n):
    num = str(n)
    return num == num[::-1]

res = 0
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j):
            aux = i*j
            if(aux > res):
                #print("%d * %d = %d" % ( i, j, aux))
                res = aux
print(res)
