from sklearn import tree
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
  'female', 'male', 'male']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)

clf_tree = tree.DecisionTreeClassifier()
clf_linear = Perceptron()
clf_log = LogisticRegression()
clf_knn = KNeighborsClassifier(n_neighbors=2)
clf_svm = SVC()

clf_tree = clf_tree.fit(X_train,y_train)
clf_linear = clf_linear.fit(X_train,y_train)
clf_log = clf_log.fit(X_train,y_train)
clf_knn = clf_knn.fit(X_train,y_train)
clf_svm = clf_svm.fit(X_train,y_train)

y_pred1 = clf_tree.predict(X_test)
y_pred2 = clf_linear.predict(X_test)
y_pred3 = clf_log.predict(X_test)
y_pred4 = clf_knn.predict(X_test)
y_pred5 = clf_svm.predict(X_test)

print (accuracy_score(y_test, y_pred1))
print (accuracy_score(y_test, y_pred2))
print (accuracy_score(y_test, y_pred3))
print (accuracy_score(y_test, y_pred4))
print (accuracy_score(y_test, y_pred5))
