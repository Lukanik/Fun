import random

dict1 = {
    'a': [1,2,3], 'b':[4,5,6]
}

c = random.choice(('a','b'))
print(c)


print(dict1[c])
