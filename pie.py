# string reversal
def reverse(word):
    x = ''
    for element in word:
        x = element + x
    return x

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

# simple number switch without using lists/arrays
def numswitch(num1,num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return(num1,num2)

swtich = numswitch(13,69)
print (swtich)