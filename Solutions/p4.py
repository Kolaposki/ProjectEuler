"""
    name='p4',
    project='Project Euler'
    date='1/9/2020',
    author='Oshodi Kolapo',
"""

"""
 A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is 9009 = 91 × 99.

   Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(numb):
    numb = str(numb)
    reverse = numb[::-1]
    return numb == reverse


maxlist = []
for i in range(1000):
    for k in range(1000):
        pal = i * k
        if is_palindrome(pal):
            if i >= 100 and k >= 100:
                maxlist.append(pal)
                print(f"{i} * {k} = {max(maxlist)}")

        else:
            pass

print(max(maxlist))
