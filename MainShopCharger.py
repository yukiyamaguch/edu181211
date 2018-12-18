import StudentCard

class MainShopCharger(object):
    insertedStudentCard = None

    def __init__(self):
        self.insertedStudentCard = None

    @staticmethod
    def insertStudentCard(studentId):
        MainShopCharger.insertedStudentCard = StudentCard.StudentCard.getStudentCard(studentId)

    @staticmethod
    def chargeMoney(money):
        if MainShopCharger.insertedStudentCard is None:
            print('学生証が挿入されていません')
        else:
            MainShopCharger.insertedStudentCard.setAccountBalance(money)

    @staticmethod
    def printAccountBalance():
        print('残高を表示します')
        print('学生名：' + MainShopCharger.insertedStudentCard.getStudentName())
        print('残高　：' + str(MainShopCharger.insertedStudentCard.getAccountBalance()))


if __name__ == "__main__":
    # 学生証インスタンス作成
    studentCard1 = StudentCard.StudentCard(0, 'tut')
    studentCard2 = StudentCard.StudentCard(1, 'tenpaku')

    # 初期残高設定
    studentCard1.setAccountBalance(1000)

    # エラー処理の表示
    MainShopCharger.chargeMoney(200)

    # 学生証1枚目の挿入とチャージ
    MainShopCharger.insertStudentCard(0)

    # 加算
    MainShopCharger.chargeMoney(1000)
    # 引き出し
    MainShopCharger.chargeMoney(-300)

    # 学生証2枚目の挿入とチャージ
    MainShopCharger.insertStudentCard(1)

    # 加算
    MainShopCharger.chargeMoney(500)
    # 引き出し
    MainShopCharger.chargeMoney(-1000)

    # 残高表示
    MainShopCharger.printAccountBalance()
