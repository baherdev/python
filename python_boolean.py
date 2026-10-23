print(3>5)
print(bool("Hello"))
print(bool(15))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myfunction():
    return True

print (myfunction())    