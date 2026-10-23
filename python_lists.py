list=['banane','orange','cerise']
tropical = ["mango", "pineapple", "papaya"]
print(list)
print(list[0])
list.append('raisin')
print(list)
print(list[1:2])#2 not included
print(list[-1])
list.insert(2,"watermelon")
print(list)
list.extend(tropical)
print(list)
list.remove('orange')
print(list)
list.pop(4)
print(list)
del list[0]
print(list)
list.clear();
print(list)
#Loop Lists
list=['banane','orange','cerise']
for x in list:
  print(x)

for i in range(len(list)):
  print(list[i])

i=0

while i < 2:
 print(list[i])
 i=i+1

 #Looping Using List Comprehension
 #A short hand for loop that will print all items in a list:
 [print(x) for x in list]

 fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#sort
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#copy method
mynewlist=fruits.copy()
print(mynewlist)
