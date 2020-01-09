import utils

"""
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.
"""


mylist =[]
for i in utils.find_prime(2000000):
    mylist.append(i)


print(sum(mylist))