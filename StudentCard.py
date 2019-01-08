import matplotlib.pyplot as plt
from keras.preprocessing import image


class StudentCard(object):
    _student_card_list = []

    def __init__(self, id, name):
        self.student_id = id        # ID
        self.student_name = name    # 名前
        self.account_balance = 0    # 残高
        self.charge_time = None     # 最終更新日
        self.img_path = None        # 画像のパス
        self.keyword_list = []      # キーワードのリスト
        self.recommend_keyword = [] # リコメンドされたキーワードのリスト
        self.character = None       # RandomCharacterで生成されるキャラクター
        StudentCard._student_card_list.append(self)

    def setAccountBalance(self, account_balance):
        self.account_balance += account_balance

    def getAccountBalance(self):
        return self.account_balance

    def getStudentName(self):
        return self.student_name

    def setChargeTime(self, charge_time):
        self.charge_time = charge_time

    def getChargeTime(self):
        print('最終チャージ時刻：'+self.charge_time)

    def setImage(self, img_path):
        self.img_path = img_path

    def getImage(self):
        return self.img_path

    def showImage(self):
        if self.img_path is not None:
            img = image.load_img(self.img_path, target_size=(299, 299))
            plt.imshow(img)
            plt.show()

    def addKeywordList(self, keyword):
        self.keyword_list.append(keyword)

    def printKeywordList(self):
        if self.keyword_list is not []:
            temp = ""
            for key in self.keyword_list:
                temp += key + ' '
            print('キーワード：'+temp)

    def getKeywordList(self):
        return self.keyword_list

    def setRecommendKeyword(self, recommend_keyword):
        self.recommend_keyword = recommend_keyword

    def getRecommendKeyword(self):
        return self.recommend_keyword

    def printRecommendKeyword(self):
        if self.recommend_keyword is not []:
            temp = ""
            for key in self.recommend_keyword:
                temp += key + ' '
            print('リコメンドされたキーワード：'+temp)

    def setCharacter(self, character):
        self.character = character

    def getCharacter(self):
        if self.character is not None:
            print('この人は'+self.character+'です')

    @classmethod
    def getStudentCard(cls, student_id):
        return StudentCard._student_card_list[student_id]
