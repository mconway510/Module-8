  class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print('Name:', self.lastName + ",", self.firstName )
        print('ID:', self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        self.ave = sum(self.scores)/numScores
        if self.ave >=90 and self.ave <= 100:
            return 'O'
        elif self.ave >= 80 and self.ave < 90:
            return 'E'
        elif self.ave >= 70 and self.ave < 80:
            return 'A'
        elif self.ave >= 55 and self.ave < 70:
            return 'P'
        elif self.ave >=  40 and self.ave < 55:
            return 'D'
        elif self.ave < 40:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())