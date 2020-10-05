class Envelope:
    def __init__(self, money):
        self.used = False
        self.money = money


    def getMoney(self):
        return self.money

    def isUsed(self):
        return self.used

    def setUsed(self):
        self.used = True

