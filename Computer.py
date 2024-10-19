class Computer:
    
    def __init__(self):
        self.__maxprice = 900
        
    def printprice(self):
        print(f"Selling Price is: {self.__maxprice}")
        
    def setMaxPrice(self, price):
        self.__maxprice = price
        

c = Computer()
c.printprice()

c.__maxprice = 1000
c.printprice()

c.setMaxPrice(1500)
c.printprice()
