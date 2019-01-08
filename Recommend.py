import gensim
import StudentCard


class Recommend(object):
    _model = gensim.models.Word2Vec.load('wiki.model')

    def __init__(self):
        pass

    @staticmethod
    def recommendRelatedKeyword(student_card):
        list = Recommend._model.most_similar(positive=student_card.getKeywordList())
        temp = []
        for key in list:
            temp.append(key[0])
        student_card.setRecommendKeyword(temp)
