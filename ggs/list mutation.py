x = [1,2,3,4,5,6,7,8,9,10]

print (len(x))
print (type(x))
print (x[3])

x[3] = "yes"
print (x)

x.insert(6,"inserted")
print (x)

x.append(99)
print (x)

y = ["avcd","hwsos"]
x.append(y)
print (x)

x.pop()
print(x)

x.pop(0)
print(x)

x.remove(99)
print(x)

y = [233,32,231,46,675,324,6,865,2]
t = sorted(y)
r = sorted(y,reverse=True)
print (t)
print (r)


del(x)
print(x)

#x.clear()
#print(x)
