x = 20

def function1 ():
    x1 = 40
    print (x)
    print (x1)

    def function2 ():
        #nonlocal x2 
        x2 = 50
        print (x)
        print (x1)
        print (x2)

    function2()

function1()

print (x)
#print (x1)
#print (x2)