from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

# Prints the name of iris species from the predicted number
def decode(num):
	for i in num:
		if i==0:
			print('Predicted Color of Flower "Setosa"')
		elif i==1:
			print('Predicted Color of Flower "Versicolor"')
		else:
			print('Predicted Color of Flower "Virginica"')
#----------------------------------------------------------

iris = load_iris()
test_ids = []

for i in range (0, 20):
	test_ids.append(i)
for i in range (50, 70):
	test_ids.append(i)
for i in range (100, 120):
	test_ids.append(i)

# Training data
train_data = np.delete(iris.data, test_ids, axis=0)
train_target = np.delete(iris.target, test_ids)

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

d1 = float(input("Enter sepal length : "))
d2 = float(input("Enter sepal width : "))
d3 = float(input("Enter petal length : "))
d4 = float(input("Enter petal width : "))

data = [d1, d2, d3, d4]
#data=[5.1,3.5,1.4,0.2]
decode(clf.predict([data]))
