# string reversal

word = 'henlo'

# without a list/array
y = 0
z = ''
while y < len(word):
    z = word[y] + z
    print(z)
    y += 1
print(z)

# with a list/array
# actually this works better as strings are converted to lists anyways
a = ''
for element in word:
    a = element + a
    print (a)