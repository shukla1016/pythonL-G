thistuple = ("apple","banana","cherry")
print(thistuple[-1])

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])
print(thistuple[2:])
print(thistuple[-4:-1])

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
for i in thistuple:
    print(i)

for i in range(len(thistuple)):
    print(thistuple[i])

if "apple" in thistuple:
    print("Apple is here!! :)")

y = (1,2,3)
thistuple+=y
print(thistuple)
