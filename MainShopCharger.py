import StudentCard
from datetime import datetime
import Recommend
import RandomCharacterGenerator


class MainShopCharger(object):
    _inserted_student_card = None

    def __init__(self):
       pass

    @staticmethod
    def insertStudentCard(student_id):
        MainShopCharger._inserted_student_card = StudentCard.StudentCard.getStudentCard(student_id)

    @staticmethod
    def chargeMoney(money):
        if MainShopCharger._inserted_student_card is None:
            print('学生証が挿入されていません')
        else:
            MainShopCharger._inserted_student_card.setAccountBalance(money)
            MainShopCharger._inserted_student_card.setChargeTime(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

    @staticmethod
    def printAccountBalance():
        print('残高を表示します')
        print('学生名：' + MainShopCharger._inserted_student_card.getStudentName())
        print('残高　：' + str(MainShopCharger._inserted_student_card.getAccountBalance()))
        MainShopCharger._inserted_student_card.getChargeTime()          # 時刻表示
        MainShopCharger._inserted_student_card.printKeywordList()       # キーワード表示
        MainShopCharger._inserted_student_card.printRecommendKeyword()  # リコメンドされたキーワード表示
        MainShopCharger._inserted_student_card.getCharacter()           # RandomCharacterGeneratorで生成されたキャラクター表示
        MainShopCharger._inserted_student_card.showImage()              # 画像表示


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

    # キーワードの登録とか
    studentCard2.addKeywordList('豊橋')
    studentCard2.addKeywordList('工学')
    studentCard2.addKeywordList('大学')
    studentCard2.addKeywordList('愛知')
    Recommend.Recommend.recommendRelatedKeyword(studentCard2)

    MainShopCharger.printAccountBalance()

    # imageの確認
    img_path = 'test.jpg'   # 適当な画像を用意してパスを入力
    studentCard2.setImage(img_path)
    #MainShopCharger.printAccountBalance()

    # RandomCharacterGenerator
    RandomCharacterGenerator.RandomCharacterGenerator.generateCharacter(studentCard2)
    MainShopCharger.printAccountBalance()