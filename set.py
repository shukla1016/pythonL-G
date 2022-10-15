thisset = {"apple","banana","cherry"}
print(thisset)

thisset = {"apple","banana","cherry","apple"}
print(thisset)

print(len(thisset))

set1 = {"apple","banana","cherry"}
set2 = {1,5,7,9,3}
set3 = {True,False,True}
print(set1,set2,set3)

myset = {"apple","banana","cherry"}
print(type(myset))

thisset = set(("apple","banana","cherry"))
print(thisset)

thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)

print("banana" in thisset)

thisset.add("orange")
print(thisset)

tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

x = thisset.pop()
print(x)
print(thisset)