import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Source of data - https://www.kaggle.com/c/digit-recognizer/data
data = pd.read_csv("datasets/train.csv").as_matrix()

clf = DecisionTreeClassifier()

#Training dataset
x_train = data[0:21000, 1:]
y_train = data[0:21000, 0]

# Testing dataset
x_test = data[21000:, 1:]
y_test = data[21000:, 0]

# Training our model
clf.fit(x_train,y_train)

# d = x_test[20]
# d.shape = (28,28)
# pt.imshow(d, cmap='gray')
# print (clf.predict([x_test[20]]))
# pt.show()

# Accuracy calculation
prediction = clf.predict(x_test)
count = 0
for i in range(0,21000):
    count+=1 if prediction[i] == y_test[i] else 0

print("Accuracy = ", (count/21000)*100)
