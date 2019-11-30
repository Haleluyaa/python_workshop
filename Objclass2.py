class Construct :
    def __init__(self) :
        print ('constructor')
    def __del__(self) :
        print('destructor')

"""
obj = Construct()

del obj
"""
class Constructor : 
    def __init__(self, name = None) :
        self.name = name
        print('Work at constructor')

    def display(self) :
        if self.name :
            print('Hi, I am %s' %self.name)
        else :
            print('Hi, I am without a name')

    def __del__(self) :
        if self.name == None : 
            print('name : None has destroyed')
        else :
            print(self.name + ' destroyed')



x = Constructor()
x.display()
y = Constructor('Thanawit')
y.display()
del x,y