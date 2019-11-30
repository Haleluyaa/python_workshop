class addObj :
    def __init__(self, x = 0, y = None, z = 0) :
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) :
        return ' '+str(self.x)+' '+str(self.y)+' '+str(self.z)
    
    def __add__(self,object) :
        x = self.x + object.x
        y = self.y + object.y
        z = self.z + object.z
        return addObj(x,y,z)



A1 = addObj(4, 'Python ', 6)
A2 = addObj(6, 'Programming', 6)
print(A1 + A2)
