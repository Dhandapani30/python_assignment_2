class Counter:
    def __init__(self,a):
        self.a=a        
    def increase(self):
        self.a+=1
        return self.a
    def decrease(self):
        self.a-=1
        return self.a
    def getValue(self):
        return self.a
a=Counter(10)
print(a.increase())
print(a.decrease())
print(a.getValue())

