class Pupil(object):
    def __init__(self, dict_name):
        self.dict = dict_name

    def  reorganization (self):
        self.schoolchild = {}
        self.student = {}
        for i in self.dict:
            if self.dict[i] == 'школьник':
                self.schoolchild.setdefault(i,self.dict[i])
            if self.dict[i] == 'студент':
                self.student.setdefault(i,self.dict[i])

    def return_schoolchild(self):
        return self.schoolchild

    def return_student(self):
        return self.student


class Schoolchild (Pupil):

    def __init__(self, dict_name):
        self.schoolchild = {}
        super().__init__(dict_name)
        super().reorganization()
        self.schoolchild = super().return_schoolchild()

    def teaching_plan(self):
        print('Список учащихся попавших под школьную учебную программу:')
        for i in self.schoolchild:
            print (i)
        print('''\nСписок предметов утвержденный по учебному плану:
         Математика
         Русский язык
         Литература
         итд''')
        print('При окончании школьного учебного курса учащиеся  перейдут в группу "студенты" и продолжить обучение там')
        for i in self.schoolchild:
            self.schoolchild[i] = 'студент'

    def return_schoolchild_student(self):
        return self.schoolchild

class Student (Pupil):

    def __init__(self, dict_name):
        self.student = {}
        super().__init__(dict_name)
        super().reorganization()
        self.student = super().return_student()

    def student_plan(self):
        print('Список учащихся попавших под студентческую учебную программу:')
        for i in self.student:
            print (i)
        print('''\nСписок предметов утвержденный по учебному плану:
         Высшая математика
         Теория базового программирования
         Иностранный язык
         итд''')
        print('При окончании студенческего обучения учащиеся  перейдут в группу "образованные". Дальнейшее обучение возможно в рамках повышения квалификации')
        for i in self.student:
            self.student[i] = 'образованный'

    def return_student_educated(self):
        return self.student





def main():
    pupil = {'Авсиевич Сергей Владимирович': 'студент', 'Горяшина Елена Витальевна': 'студент', 'Калинин Антон Александрович': 'школьник',"Крамынина Галина Николаевна": "студент", "Лебедев Вадим Сергеевич": "студент",'Воротченко Светлана Олеговна': 'школьник'}

    school = Schoolchild(pupil)
    school.teaching_plan()
    print('\n')

    institute = Student(pupil)
    institute.student_plan()



main()
