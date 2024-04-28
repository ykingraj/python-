'''
____________________________________________________________________________________________________________________
                                                    #Mutable Objects:#
____________________________________________________________________________________________________________________
Mutable objects are those whose state can be modified after creation.
When you modify a mutable object, you're actually changing the object itself, not creating a new one.
While changing the contents of these datatypes, the actual content which was initelly stored is changed.
Lists (list)
Dictionaries (dict)
Sets (set)
Byte Arrays (bytearray)
User-defined classes (if designed to be mutable)
Deques (collections.deque)
Arrays (array.array)
Numpy arrays (numpy.ndarray)
DataFrames (pandas.DataFrame)
Mutable sequences (collections.UserList, collections.UserString, collections.UserDict, etc.)
'''
x = [1,2,3,4,5]

y= x
print (x) # 1,2,3,4,5
print (y) # 1,2,3,4,5

x[2] = 10
print (x) # 1,2,10,4,5
print (y) # 1,2,10,4,5


'''
____________________________________________________________________________________________________________________
                                                    #Immutable Objects:#
____________________________________________________________________________________________________________________
Immutable objects, on the other hand, cannot be changed after they are created.
When you perform operations that seem to modify immutable objects, you're actually creating new objects.
While changing the contents of these datatypes, the actual content which was initelly stored is not changed rather a memory address is assigned to new value and the old value is cleared of the memory if there is no refferance to it by the garbage collection.
Integers (int)
Floating-point numbers (float)
Complex numbers (complex)
Strings (str)
Tuples (tuple)
Frozensets (frozenset)
Bytes (bytes)
Booleans (bool)
NoneType (None)
Enums (enum.Enum)
Named tuples (collections.namedtuple)
Immutable sequences (collections.namedtuple, collections.Counter, collections.UserString, etc.)
'''
x= 10
y = x
print (x) # output = 10
print (y) # output = 10

x= 2
print (x) # output = 2
print (y) # output = 10

