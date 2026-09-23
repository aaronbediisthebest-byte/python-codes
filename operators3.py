x=5
if (type(x)is int):
    print("true")
else:
    print("false")
a=6
b=7
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a<<b)
print(a>>b)
print ("enter marks collected in 3 subjects")
maths=int(input())
sport=int(input())
art=int(input())
tot=maths+sport+art
avg=int(tot/3)
validrange=range(0,101)
if avg not in validrange:
    print("invalid input!")
elif avg in range(91,101):
    print("your grade is A1")
elif avg in range(81,91):
    print("your grade is A2")
elif avg in range(71,81):
    print("your grade is b1")
elif avg in range (61,71):
    print("your grade is b2")
elif avg in range(51,61):
    print("your grade is c1")
elif avg in range(41,51):
    print("your grade is c2")
elif avg in range(31,41):
    print("your grade is d1")
