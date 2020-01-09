import math

"""
      145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

   Find the sum of all numbers which are equal to the sum of the factorial of
   their digits.

   Note: as 1! = 1 and 2! = 2 are not sums they are not included.   
"""


def find(num: int):
    mylist, newlist = [], []
    number = str(num)
    for k in number:
        mylist.append(int(k))
    for i in mylist:
        newlist.append(math.factorial(i))
    return sum(newlist)



o_list = []
for r in range(3, 100000):
    if r == find(r):
        o_list.append(r)

print(o_list)
print(sum(o_list))
