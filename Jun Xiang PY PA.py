class CalUtils:

    def __init__(self):
        self.name = []
        self.height = 0
        self.total_student_count = 0
        self.total_student_height = []

    def calAvgHeight(self):
        txtfile = open('listOfStudentHeight.txt', 'r')

        for y in txtfile.readlines():
            line = y.split('\t')
            self.name.append(line[0])
            n = float(line[1])
            self.total_student_height.append(n)

        self.total_student_count = len(self.name)

        avg_height = sum(self.total_student_height) / self.total_student_count

        txtfile.close()

        print(round(avg_height, 2))

    def main(self):

        start = input("Do you want to input new student name? Y/N: ").upper()

        if start == 'Y':
            txtfile = open('listOfStudentHeight.txt', 'a')
            name = input('Enter a name: ')
            height = str(input('Enter height: '))
            txtfile.write = (name + '\t' + height)

        else:
            exit()

        if start == 'N':
            txtfile = open('listOfStudentHeight.txt', 'r')

        for y in txtfile.readlines():
            line = y.split('\t')
            self.name.append(line[0])
            n = float(line[1])
            self.total_student_height.append(n)

        self.total_student_count = len(self.name)

        new_avg_height = sum(self.total_student_height) / self.total_student_count

        txtfile.close()

        print(round(new_avg_height, 2))


x = CalUtils()
x.calAvgHeight()
x.main()