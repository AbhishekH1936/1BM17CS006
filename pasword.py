import random
import string
s=string.punctuation
x=string.digits
y=string.ascii_lowercase
z=string.ascii_uppercase
a=(s+x+y+z)
#print(a)
length =int(input('enter the length'))
p =  "".join(random.sample(a,length ))
print( p)
