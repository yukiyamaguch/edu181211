import keras
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.xception import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt
import StudentCard


# 説明しよう！
# RandomCharacterGeneratorとは！！
# ImageNetに顔画像を入れるとだいたいわけわからんクラスに分類されることを利用した、
# ランダムキャラ生成器である！！！
class RandomCharacterGenerator(object):
    _model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)  # 入力は(299,299,3)、widthとheightが71以上で3チャネルならOK
    _img_path = None
    _img = None
    _preprocess_image = None
    _result = None

    def __init__(self):
        pass

    @staticmethod
    def setImage(path):     # 画像の読み込み
        RandomCharacterGenerator._img_path = path
        RandomCharacterGenerator._img = image.load_img(path, target_size=(224, 224))

    @staticmethod
    def showImage():        # 画像の出力
        plt.imshow(_img)
        plt.show()

    @staticmethod
    def preprocessImage():  # 画像の前処理
        preprocess_image = image.img_to_array(RandomCharacterGenerator._img)
        preprocess_image = np.expand_dims(preprocess_image, axis=0)
        RandomCharacterGenerator._preprocess_image = preprocess_input(preprocess_image)

    @staticmethod
    def predictImage():     # 画像の予測
        preds = RandomCharacterGenerator._model.predict(RandomCharacterGenerator._preprocess_image)
        RandomCharacterGenerator._result = decode_predictions(preds, top=1)[0][0][1]

    @staticmethod
    def generateCharacter(student_card):
        RandomCharacterGenerator.setImage(student_card.getImage())
        RandomCharacterGenerator.preprocessImage()
        RandomCharacterGenerator.predictImage()
        student_card.setCharacter(RandomCharacterGenerator._result)

