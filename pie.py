# string reversal
def reverse(word):
    x = 0
    y = ''
    while x < len(word):
        y = word[x:x+1] + y
        x += 1
    return y

result = reverse('henlo')
print(result)

# odd-even checker
def oddeven(num):
    x = ''
    for element in num:
        if element % 2 == 0:
            x += '%d is even \n' % (element)
        else:
            x += '%d is odd \n' % (element)
    return x
    
check = oddeven([15,20,25])
print(check)