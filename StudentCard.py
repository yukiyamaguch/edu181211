class StudentCard(object):
    StudentCard_list = []

    def __init__(self, id, name):
        self.studentId = id
        self.studentName = name
        self.accountBalance = 0
        StudentCard.StudentCard_list.append(self)

    def setAccountBalance(self, accountBalance):
        self.accountBalance += accountBalance

    def getAccountBalance(self):
        return self.accountBalance

    def getStudentName(self):
        return self.studentName

    @classmethod
    def getStudentCard(cls, studentId):
        return StudentCard.StudentCard_list[studentId]