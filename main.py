class myClass:
    __privateVar = 27
    def __privMeth(self):
        print("im inside class myClass")
    def hello(self):
        print("Private Variable value: ",myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privMeth
class Computer:
    def __init__(self):
        self.__maxprice = 900
        def sell(self):
            print("Selling Price: {}".format(self.__maxprice))
        def setMaxPrice(self, price):
            self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell
c.setmaxprice(1000)
c.sell()