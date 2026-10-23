dictionary={
    "one":"Value1",
    "two":"Value2",
    "three":"Value3",

}
print(dictionary)
print(dictionary["one"])
print(dictionary.keys())
print(dictionary.values())
dictionary[ "four"]="Value4"
print(dictionary.values())    
dictionary.pop("three")
print(dictionary.values())    