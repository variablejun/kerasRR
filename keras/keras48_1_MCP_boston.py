
from re import M
from tensorflow.keras.models import Sequential, Model,load_model
from tensorflow.keras.layers import Dense, SimpleRNN, Dropout, LSTM, GRU, Input, Conv1D
import numpy as np 

from sklearn.datasets import load_boston
datasets = load_boston()

#1.data
x = datasets.data
y = datasets.target
'''

'''
print(np.max(x))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,
train_size = 0.95, random_state=66)

x_train = x_train.reshape(480,13,1) #
x_test = x_test.reshape(26, 13, 1)

'''

'''

'''

model = Sequential()
model.add(Conv1D(16,2,activation = 'relu',input_shape=(13,1)))
model.add(LSTM(64))
model.add(Dense(32,activation='relu'))
model.add(Dense(16,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(2,activation='relu'))
model.add(Dense(1 ,activation='relu'))

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
es = EarlyStopping(monitor='val_loss', patience=30, mode='min', verbose=3)
cp = ModelCheckpoint(monitor='val_loss', save_best_only=True,mode='auto', filepath='./_save/ModelCheckpoint/keras47_MCP.hdf5')

import time
starttime = time.time()
model.compile(loss = 'mse', optimizer = 'adam')
hist = model.fit(x_train, y_train, epochs=1000, batch_size=64, validation_split=0.003, verbose=2,callbacks=[es,cp]) 
model.save('./_save/ModelCheckpoint/keras47_Model_Save.h5')
'''
model = load_model('./_save/ModelCheckpoint/keras47_Model_Save.h5')
#model = load_model('./_save/ModelCheckpoint/keras47_MCP.hdf5')
loss = model.evaluate(x_test, y_test,batch_size=64) 

print('loss : ', loss)
y_pred = model.predict(x_test) 

# y_pred = scaler.transform(y_pred)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print("r2score ", r2)

'''
1D로 수정후
Epoch 00132: early stopping
1/1 [==============================] - 0s 22ms/step - loss: 18.0583
걸린시간 10.305974245071411
loss :  18.058317184448242
r2score  0.8599481605369796

MCP
1/1 [==============================] - 2s 2s/step - loss: 23.3620
loss :  23.361961364746094
r2score  0.8188155970742481

model Save
1/1 [==============================] - 2s 2s/step - loss: 19.9358
loss :  19.935789108276367
r2score  0.8453873799642385
'''