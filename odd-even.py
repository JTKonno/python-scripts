# odd-even checker

"""
#single number
num = 15

if num % 2 == 0:
    print('%d is even' % (num))
else:
    print('%d is odd' % (num))
"""


#list/array
num = [1,2,3,4,5,6,7,8,9,10]
x = 0

"""
#while version
while x < len(num):
    if num[x] % 2 == 0:
        print('%d is even' % (num[x]))
    else:
        print('%d is odd' % (num[x]))
    x += 1
"""

#for version
for element in num:
    if element % 2 == 0:
        print('%d is even' % (element))
    else:
        print('%d is odd' % (element))