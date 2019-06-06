class CalUtils:
    def __init__(self):
        self.name = ""
        self.height = 0.00
        self.total_student_count = 0
        self.total_student_height = []
        self.start = ""

    def calAvgHeight(self):
        txtfile = open('listOfStudentHeight.txt', 'r')
        for y in txtfile.readlines():
            line = y.split('\t')
            n = float(line[1].replace("\n", ""))
            self.total_student_height.append(n)
            self.total_student_count = self.total_student_count + 1
        txtfile.close()

        avg_height = sum(self.total_student_height) / self.total_student_count
        print("the average student height is " + str(round(avg_height, 2)) + "m for " + str(self.total_student_count) + "students.")

        self.name = str(input("enter name: "))
        self.height = float(input("enter height: "))

        k = open("listOfStudentHeight.txt", "a")
        k.writelines(str(self.name).upper() + "\t" + str(self.height) + "\n")
        k.close()

        self.total_student_count = 0
        self.total_student_height = []

        self.start = input("Do you want to input new student name? Y/N: ").upper()
        if self.start == 'Y':
            self.calAvgHeight()
        elif self.start == 'N':
            print("the average student height is " + str(round(avg_height, 2)) + "m for " + str(self.total_student_count) + "students.")

            exit()


x = CalUtils()
x.calAvgHeight()
