class Person:
    def __init__(self, n,l,d):
        self.name = n
        self.lastname = l
        self.dateofbirth = d

    def printdetails(self):
        print(f"Name :{self.name}")
        print(f"Last Name :{self.lastname}")
        print(f"Date of birth :{self.dateofbirth}")

    def is_eligible(self, age):
        if age >= 18:
            return True
        else:
            return False


x = Person("X", "D", "01 Jan, 2008")

x.printdetails()
print(x.is_eligible(14))
