class Employee:
    def __init__(self, id, first, last, year):
        self.id = id
        self.firstName = first
        self.lastName = last
        self.hireYear = year

    def __str__(self):
        return f'{self.id}, {self.firstName}, {self.lastName}, {self.hireYear}'

    def getid(self):
        return self.id

    def getfirstname(self):
        return self.firstName

    def getlastname(self):
        return self.lastName

    def gethireyear(self):
        return self.hireYear

    def setid(self, newid):
        self.id = newid

    def setfirstname(self, newfirst):
        self.firstName = newfirst

    def setlastname(self, newlast):
        self.lastName = newlast

    def sethireyear(self, newyear):
        self.hireYear = newyear