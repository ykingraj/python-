dict = {
    "name":"yash",
    "age":20,
    "trade":"csa",
    "course":"cits"
}

print (dict["name"])

print (dict.keys())

print (dict.values())

print (dict.items())

d = dict.copy()

dict.pop("trade")
print(dict)

dict.popitem() # removes last item
print(dict)

dict.clear()
print(dict)
#print (d)