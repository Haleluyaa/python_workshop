import ObjInherParent

class Rectangle (ObjInherParent.Shape) :

    def area(self) :
        return (self.width * self.height)


#Main Program
print('Area of Rectangle Calculation \nPlease enter values for calculate.')
w = int(input('Enter width : '))
h = int(input('Enter height : '))
rect = Rectangle(w,h)
print('Rectangle area : %s' %rect.area())
