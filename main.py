class Student:
    group = "C2016"
    counter = 0
    def __init__(self, age, height, name=None):
        self.name = name
        self.age = age
        self.height = height
        Student.counter += 1
        print(id("Объект был создан "))
    def grow(self):
        print("shfjdlkseajfklasjd")
        self.height += 10
    def __str__(self):
        return f"I'm {self.name}. My age is {self.age}"
    def __del__(self):
        print("Удален объект")

print(Student.group)
nick = Student(16,  165, "Nick")
print(nick)
# print(nick.age)
# print(nick.height)
# print(nick.name)
# print(nick.group)
# kate = Student(17, 175, "Ekatirina")
# print(kate.height)
# print(kate.age)
# print(kate.name)
# print(kate.group)
# elena = Student(18, 160, "Elena")
# print(Student.counter)
# print("Nick height", nick.height)
# nick.grow()
# print("Nick height", nick.height)
