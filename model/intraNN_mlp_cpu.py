#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import keras
import tensorflow as tf
from IPython.display import display

from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())

from keras import backend as K

from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from keras.datasets import mnist
from keras.utils import np_utils
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy 
import matplotlib.pyplot as plt
import pandas as pd
import glob
import os 

seed = 0
tf.set_random_seed(seed)

# model-compile parameter sets
model_metrics = 'acc'
num_epochs = 10000
num_batch = 100
num_split = 0.2

# train set
org_inp_num = 5
path = r'C:\srcDL\int5_h' 
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
df_from_each_file = (pd.read_csv(f, header=None) for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
concatenated_df.columns = ["BTS", "BTD", "BSR", "MTD", "CBF", "Class"]
df = concatenated_df.sample(frac=1).values

# model I: 5x30x1
inp_num = 5
updated_columns = ["BTS", "BTD", "BSR", "MTD", "CBF",  "Class"]
x = df[:, [0,1,2,3,4]]
y = df[:, org_inp_num]

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=num_split, random_state=seed)

model = Sequential()
model.add(Dense(30, input_dim=inp_num, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=[model_metrics])
history = []
history.append(model.fit(X_train, Y_train, validation_data=(X_test, Y_test), 
                         epochs=num_epochs, batch_size=num_batch))
model.save('model_5x30x1.h5')  
eval_model = []
eval_model.append(model.evaluate(X_test, Y_test)[1])
print("\nTest Accuracy: %.4f" % eval_model[0])
del model       

