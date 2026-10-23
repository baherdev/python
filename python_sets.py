#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
thisisaset={"apple",'banane',1,3,True}
print(thisisaset)
print(len(thisisaset))
#Once a set is created, you cannot change its items, but you can add new items.
thisisaset.add(4)
print(thisisaset)
thisisaset.remove('apple')
print(thisisaset)

#frozenset is an immutable version of a set.
## Like sets, it contains unique, unordered, unchangeable elements.
## Unlike sets, elements cannot be added or removed from a frozenset.

list=['banane','orange','cerise']
x = frozenset(list)
print(x)
print(type(x))