#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = "apple", "banana", "cherry"
print(thistuple)


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[1])
print(thistuple[-4:-1])

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#Unpacking a Tuple
## Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
##If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)