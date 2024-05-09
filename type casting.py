sting =  "abc "
number = 85
boolean = False

listmix = [1,2,3,"a","b"]
listalpha = ["a","b","c"] 
listnum = [1,2,3,4,5]

tuplemix = (1,2,3,"a","b")
tuplealpha = ("a","b","c") 
tuplenum = (1,2,3,4,5)

dictonary = {"name" : "yash" ,
             "age" : 20}

'''
# str() type casting
y = str( number)
print(y) #output 79
print (type(y)) #output <class 'str'>

y = str( boolean)
print(y) #output True
print (type(y)) #output <class 'str'>

y = str( listmix)
print(y) #output [1, 2, 3, 'a', 'b']
print (type(y)) #output <class 'str'>

y = str( listalpha)
print(y) #output ['a', 'b', 'c']
print (type(y)) #output <class 'str'>

y = str( listnum)
print(y) #output [1, 2, 3, 4, 5]
print (type(y)) #output <class 'str'>

y = str( tuplealpha)
print(y) #output ('a', 'b', 'c')
print (type(y)) #output <class 'str'>

y = str( tuplemix)
print(y) #output (1, 2, 3, 'a', 'b')
print (type(y)) #output <class 'str'>

y = str(dictonary)
print(y) #output {'name': 'yash', 'age': 20}
print (type(y)) #output <class 'str'>

y = str( tuplenum)
print(y) #output (1, 2, 3, 4, 5)
print (type(y)) #output <class 'str'>
'''
'''
# int() type casting
#y = int( sting)
#print(y) #output error
#print (type(y)) #output error 

y = int( boolean)
print(y) #output 1 for true and 0 for false 
print (type(y)) #output <class 'int'>

#y = int( listmix)
#print(y) #output error  (int() argument must be a string, a bytes-like object or a real number, not 'list')
#print (type(y)) #output error 

#y = int( listalpha)
#print(y) #output error  (int() argument must be a string, a bytes-like object or a real number, not 'list')
#print (type(y)) #output error

#y = int( listnum)
#print(y) #output error  (int() argument must be a string, a bytes-like object or a real number, not 'list')
#print (type(y)) #output error

#y = int( tuplealpha)
#print(y) #output error (int() argument must be a string, a bytes-like object or a real number, not 'tuple')
#print (type(y)) #output error 

#y = int( tuplemix)
#print(y) #output error (int() argument must be a string, a bytes-like object or a real number, not 'tuple')
#print (type(y)) #output error 

y = int(dictonary)
print(y) #output error (int() argument must be a string, a bytes-like object or a real number, not 'dict')
print (type(y)) #output error 

y = int( tuplenum)
print(y) #output error (int() argument must be a string, a bytes-like object or a real number, not 'tuple')
print (type(y)) #output error 
'''
'''
# bool() type casting
y = bool( number)
print(y) #output if 0 then false esle true for any number
print (type(y)) #output <class 'bool'>

y = bool( sting)
print(y) #output if string is empty then false else for anything in string then true
print (type(y)) #output <class 'bool'>

y = bool( listmix)
print(y) #output if list is empty then false and for anything in list then true
print (type(y)) #output <class 'bool'>
# same for tuples

y = bool( dictonary)
print(y) #output if dictnoary is empty then false and for anything in list then true
print (type(y)) #output <class 'bool'>
'''
'''
#list() type casting
#y = list( number)
#print(y) #output 'int' object is not iterable
#print (type(y)) #output error

y = list( sting)
print(y) #output ['a', 'b', 'c', ' ']
print (type(y)) #output <class 'list'>

#y = list( boolean)
#print(y) #output 'bool' object is not iterable
#print (type(y)) #output error

y = list( tuplenum)
print(y) #output [1, 2, 3, 4, 5]
print (type(y)) #output <class 'list'>

y = list( dictonary)
print(y) #output ['name', 'age'] only keys are made elements of the list
print (type(y)) #output <class 'list'>
'''
'''
#tuple() type casting
#works same as list()
'''
'''
#float() type casting
#y = float( sting)
#print(y) #output error
#print (type(y)) #output error

y = float( number)
print(y) #output 85.0
print (type(y)) #output <class 'float'>
'''