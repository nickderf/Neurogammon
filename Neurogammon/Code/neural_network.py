# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S_txO2BP6D6Sw4NWXiQaR3LnGwtN-XqW
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.optimizers import SGD
import keras
import math 
from sklearn.preprocessing import scale

dataset = pd.read_excel('/content/sample.xlsx')

X = dataset.iloc[:, 1:32]
y = dataset.iloc[:, 32:33]



print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
#print(X_train)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
#X_train= scale(X_train)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU,PReLU,ELU
from keras.layers import Dropout



classifier = Sequential()


classifier.add(Dense(output_dim = 6,  kernel_initializer = 'he_uniform',activation='relu',input_dim = 31))


classifier.add(Dense(output_dim = 6,  kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(output_dim = 100,  kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(output_dim = 6,  kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(output_dim = 600,  kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(output_dim = 100000,  kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(output_dim = 1,  kernel_initializer = 'glorot_uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'Adamax', loss = 'binary_crossentropy', metrics = ['accuracy'])

model_history=classifier.fit(X_train, y_train,validation_split=0.33, batch_size = 10, nb_epoch = 15)


print(model_history.history.keys())




plt.plot(model_history.history['loss'])
plt.plot(model_history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


y_pred = classifier.predict(X_test)
print(y_pred,y_test)
#y_pred =round(y_pred)
l=np.array(y_pred).round()
print(l)

from sklearn.metrics import accuracy_score
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.4)
score=accuracy_score(y_pred,y_test)
print(score)
score = classifier.evaluate(X_test, y_test, batch_size=10)
print(score)