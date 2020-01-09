import utils

"""
  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
   that the 6th prime is 13.

   What is the 10 001st prime number?

"""
count = 0
#prime_numb = utils.find_prime(10000)
for i in range(10002):
    if i in utils.find_prime(10001):
        count += 1
        print(count)

        if count == 10001:
            print(f"{count}st prime number is {i}")
            break
