class shop : 
    'This is my shop class'
    shopName = ''

class productB : 
    'Product of my company'
    prodID = 0

    def __init__(self, name, price) :
        #Define instance or constuctor
        self.name = name
        self.price = price

        productB.prodID += 1

    def dispProduct(self) :
        print ('Name : %s' %self.name +', Price : %d' %self.price)

    def salesAmount(self, amount) :
        return (self.price * amount)




myShop = shop()
myShop.shopName = 'Thanawit store'          #Define variable name 'shopName' of myShop
print('My Shop is : %s' %myShop.shopName)   #Print shop name from shopName variable
book1 = productB('Nattha shop', 299)        #Create New object 'book1' and define initial product detail
print('ProductID %d' %book1.prodID)         #Print ProductID value from book1 obj
book1.dispProduct()                         #Print Name and Price of disProduct method
print('saleAmount : %d' %book1.salesAmount(255))
book2 = productB('Microsoft Word', 179)     #Create New Object name 'book2' and define initial product detail
print ('ProductID %d' %book2.prodID)
book2.dispProduct()
print('salesamount : %d' %book2.salesAmount(479))



