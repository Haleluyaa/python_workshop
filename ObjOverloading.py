class rec :
    def __init__(self, width, height) : 
        self.width = width
        self.height = height

    def __str__(self) :
        return "({0}, {1})".format(self.width,self.height)



A1 = rec(4,6)
A2 = rec(6,6)
#A1 + A2
print(A1)
print(A2)

