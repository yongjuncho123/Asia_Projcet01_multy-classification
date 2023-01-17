import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras.layers import *
from keras.models import *
import pickle
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print(tensorflow.__version__)



X_train, X_test, Y_train, Y_test = np.load('models/novel_data_141_wordsize_8470_test.npy', 
allow_pickle=True)

print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model = keras.models.Sequential()
model.add(Embedding(8470, 300, input_lenghth=141))
model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu'))
model.add(MaxPool1D(pool_size=1))
model.add(LSTM(128, activation='tanh', return_sequences=True))
model.add(Dropout(0.5))
model.add(LSTM(64, activation='tanh', return_sequences=True))
model.add(Dropout(0.5))
model.add(LSTM(64, activation='tanh'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(12, activation='softmax'))
model.summary()


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size=128,
                     epochs=10, validation_data=(X_test, Y_test))
model.save('./models/Munpia_model_{}.h5'.format(
    fit_hist.history['val_accuracy'][-1]))
plt.plot(fit_hist.history['val_accuracy'], label='val_accuracy')
plt.plot(fit_hist.history['accuracy'], label='accuracy')
plt.legend()
plt.show()