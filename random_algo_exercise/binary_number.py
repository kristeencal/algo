
# Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation


import sys

num = int(raw_input())

result = 0
maximum = 0

while num > 0:
    if num %2 == 1:
        result += 1
        if result > maximum:
            maximum = result
    else:
        result = 0

    num //=2


print maximum
