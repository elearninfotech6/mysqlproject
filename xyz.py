class p1:
    def m(self):
        print('parent1')

class p2:
    def m2(self):
        print('parent2')

class c(p1,p2):
    def m3(self):
        print('child')

obj=c()
obj.m3()
obj.m()
obj.m2()



