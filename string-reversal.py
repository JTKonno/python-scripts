## string reversal

x = 'henlo'
mylist = []
y = 0
z = ''
while y < len(x):
    """
    ## with a list/array
    mylist.append(x[y:y+1])
    print (mylist)
    y += 1
    """

    ## without a list/array
    z = x[y:y+1] + z
    print(z)
    y += 1

print(mylist)
print(z)