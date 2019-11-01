class Student:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.dep = "Програмирование"
        self.year_of_ent = "2017 г."
    
    def get_student_info(self):
        print(self.name + self.last_name + " поступил в " + self.year_of_ent + "на факультет " + self.dep)

student1 = Student("Вася ", "Иванов")
student1.get_student_info()

