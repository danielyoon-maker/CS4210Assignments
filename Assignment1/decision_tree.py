#-------------------------------------------------------------------------
# AUTHOR: Daniel Yoon
# FILENAME: decision_tree.py
# SPECIFICATION: converts contact-lens.csv to processable dat
# FOR: CS 4200- Assignment #1
# TIME SPENT: 7 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from abc import abstractproperty
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
for i in range (0, 10):
  X.append([])

for i in range(0,4):
  count = 1
  symbolDict = {}
  for j in range(0,10):
    if db[j][i] not in symbolDict:
      symbolDict[db[j][i]] = count
      count += 1
    X[j].append(symbolDict.get(db[j][i]))

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
for x in db:
  if x[4] == "Yes":
    Y.append(1)
  else:
    Y.append(0)
print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()