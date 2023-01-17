import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
import os

os.environ['TF_CPP_MINLOG_LEVEL'] = '2' # 텐서플로우 ERROR, WARNING, INFO 출력 제어
pd.set_option('display.unicode.east_asian_width', True) # 유니코드 넓이 조절

df = pd.read_csv('./Moonpia_clawing_data/Munpia_pre_final.csv')
print(df.tail(5))

X = df['titles']
Y = df['genres']

encoder = LabelEncoder() # 카테고리 데이터를(여기선 장르) 수치화(로맨스는 1, 무협은 2 이런식으로)
labeled_Y = encoder.fit_transform(Y)
print(labeled_Y)
# fit, transform, fit_transform 설명
# https://david-kim2028.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%B2%98%EB%A6%AC-fit-fittransform-transform%EC%9D%98-%EA%B0%9C%EB%85%90-%EC%9D%B5%ED%9E%88%EA%B8%B0

label = encoder.classes_
print(label)
# encoder.classes_ : 문자열이 어떤 숫자 값으로 인코딩 됐는지 보여줌

with open('./models/encoder_labeled_data', 'wb') as f:
    pickle.dump(encoder, f)
# pickle은 파이썬 객체 저장 방법 wb: write binary(이진, 이진법의 그 이진임)
# pickle.dump(객체, 파일) : 저장 / pickle.load(파일) : 불러오기

onehot_Y = to_categorical(labeled_Y)
print(onehot_Y[0])
# to_categorical : 원핫인코딩 함수 / 파라미터 크기만큼 0으로 배열된 크기를 만들고 파라미터 값에만 1로 만듬

okt = Okt()
for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)
# morphs는 형태소 분리기, 옵션엔 norm과 stem / norm = 문장 정규화, stem = 단어 어간 추출 기능
print(X)

stopword = pd.read_csv('./stopwords.csv', index_col = 0)

for j in range(len(X)):
    words_X = []
    for k in range(len(X[j])):
        if len(X[j][k]) > 1:
            if X[j][k] not in list(stopword['stopword']):
                words_X.append(X[j][k])
    X[j] = ' '.join(words_X)

print(words_X)
# stopword로 불용어 제거 / 형태소 분리된 X에서 불용어를 제거하고 하나로 합쳐서 출력

token = Tokenizer()
token.fit_on_texts(X) # fit_on_texts은 문자 데이터를 입력받아 리스트로 변환
tokened_X = token.texts_to_sequences(X) 
# texts_to_sequences는 텍스트 안의 단어들을 연속된 숫자 형태로(시퀀스) 변환( 사과를 먹다 -> [4,2,1,3])
print(tokened_X)

wordsize = len(token.word_index) + 1

with open('./models/encoder_labeled_data', 'wb') as f:
    pickle.dump(token, f)

max = 0
for i in range(len(tokened_X)):
    if max < len(tokened_X[i]):
        max = len(tokened_X[i])
print(max) # 141
# 위에 시퀀스의 최대 길이값을 구하고 이후에 padding을 통해 각 시퀀스 길이를 똑같이 할 것이다.(길이르 똑같이 맞추어 하나의 행렬)

X_pad = pad_sequences(tokened_X, max)
print(X_pad)
# 패딩을 해줘 길이를 위에 max값고 똑같이 모두 같게 만듬

X_train, X_test, Y_train, Y_test = train_test_split(
    X_pad, onehot_Y, test_size = 0.1)

print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)


xy = X_train, X_test, Y_train, Y_test

np.save('./models/novel_data_{}_wordsize_{}_test'.format(max, wordsize), xy)