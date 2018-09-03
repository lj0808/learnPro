class Student(object):
    name = ''
    age = 0
    _weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.w = w


    def speak(self):
        print(self)
        print("%s 说：我 %d 岁。"%(self.name,self.age))


t = Student('runob',10,30)
t.speak()