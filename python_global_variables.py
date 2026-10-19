x= "Awesome"

def myfunction():
    print("Python is",x)

myfunction()

def myfunction():
    x='is good'
    print("Python is",x)

myfunction()

print("Python is",x)

#If you use the global keyword, the variable belongs to the global scope:

def myfunction():
    global x
    x='is wow'
    print("Python is",x)

myfunction()
print("Python is",x)