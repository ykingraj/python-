#String manipulation

# concatenation
x = "yash"
y = "raj"
print (x+y)

# String Formating
name = "Yash"
age = 20
print("My age is {} and my age is {}".format(name,age))

# Split function
a = "yash, ravi, aditya, dev, aaquib,1,2,345"
lst = a.split(",")
print (lst)

# upper function
str = "abcd"
print(str.upper())

# Lower function
str = "ABCDDD"
print (str.lower())

# replace function
str = "abcd"
print (str.replace("b","123"))

# find function
str = "abcdefghijk"
print (str.find("d"))