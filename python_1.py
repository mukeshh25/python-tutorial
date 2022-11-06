# 
from importlib.metadata import packages_distributions


print('Hello,My Dad!')

a = "mukesh"
b = 5
print(a)
print(b)

c = str(6)
d = int(6)
e = float(6)
print(c)
print(d)
print(e)

f = 5
g = "Mukesh"
h = 5.0
print(type(f))
print(type(g))
print(type(h))

i = "Mukesh"
print(i)
#double quotes are the same as single quotes:
i = "mukesh"
print(i)

j = 6
J ="Gulshan"
#A will not overwrite a
print(j)
print(J)

my_var = "Mukesh"
myvar = "Mukesh"
MYVAR = "Mukesh"
_My_var = "Mukesh"
print(my_var)
print(myvar)
print(MYVAR)
print(_My_var)

my_var = "Gulshan"
print(my_var)
# variable are not allowed ex 2my_var ="Shreya" / print(2my_var)
# Hence 2 is variable 

my_variable_name = "Mukesh"
print(my_variable_name)

k , l , m ="Orange" , "Peanuts" , "Mangoes"
print(k)
print(l)
print(m)

birds = "peacock" , "maina" , "peagion"
n , o ,p = birds
print(n)
print(o)
print(p)

q = "awesome"
def myfunc():
    print(" I am " + q)
myfunc()

def myfunc():
  global r
  r = "fantastic"

myfunc()

print("Python is " + r)

s = 162E6
print(type(s))



#convert from int to float:
u = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(u)
print(y)
print(z)

print(type(u))
print(type(y))
print(type(z))



'''int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals'''
print('Hello')


for v in "banana":
  print(v) 

w = "Hello world"
print(w[6])

t = "Mukesh kumar"
print(len(t))

print("mukesh")

q = "Hello, World!"
print(q.lower())

q = "hello,world!"

r = """The oldest classical British and Latin writing
 had little or no space between words and could be written in
  boustrophedon (alternating direction."""
print(r)


txt = "the things in my heavy life "
print("man" in txt)

print("\U0001F917")
print("\U0001F637")
print("\U0001f62A")
print("\U0001F618")
print("\U0001F600")
print("\U0001F413")

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

print(a.replace("H", "M"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

c ="Mukesh"
d ="World"
m = c + d
print(m)

x = "Hello"
y = "World"
z = x + " "  + y
print(z)

age = "16 years old"
txt ="My name is Mukesh , and I am {} " 
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format( quantity, itemno, price))


myorder = "I want to pay{2} dollars for {0} piece of item {1}"
print(myorder.format( quantity , itemno , price ))

