x = 20

def function1 ():
    x1 = 40
    x = "changed"
    print (x , " Local function 1 call")
    print (x1)

    def function2 ():
        #nonlocal x1 
        x1 = 44
        x2 = 50
        print (x , "in fun 2")
        print (x1 , " x1 in fun 2")
        print (x2)

    
    function2()
    print (x1 ," x1 after fun2")
    
    x = "again changed"
    print (x , " after fun2")
    


function1()
print (x, " globel call")
#print (x1)

'''
x = 20

def function1 ():
    x1 = 40
    global x 
    x = "changed"
    print (x , " Local function 1 call")
    print (x1)

    def function2 ():
        #nonlocal x2 
        x2 = 50
        #print (x)
        #print (x1)
        #print (x2)
    function2()


function1()
print (x, " globel call")
'''