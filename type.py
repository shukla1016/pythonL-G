x = 1
y = 65483456583456498464343
z = -486443
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
x1 = 35e3
y1 = 12E4
z1 = -87.7e100
print(type(x1))
print(type(y1))
print(type(z1))

x = 3+5j
y = 5j
z = -5j

x = 1.0
y = 1.0
z = 1.0

a = int(x)
b = float(y)
c = complex(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

print(type(x))
print(type(y))
print(type(z))
print(bool("Hello"))
print(bool(12))

x = {1,2,3,4,5}
y = { 5,6,7,4,2}
z = x.union(y)
print (z)
z = x.intersection(y)
print (z)