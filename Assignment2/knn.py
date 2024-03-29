#-------------------------------------------------------------------------
# AUTHOR: Daniel Yoon
# FILENAME: knn.py
# SPECIFICATION: fufilled assignment requirements as specified
# FOR: CS 4210- Assignment #2
# TIME SPENT: 10 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

error = 0 
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []
    Y = []
    symbolDict = {
        '+' : 1,
        '-' : 2
    }
    for j in range(len(db)):
        if j != i:
            appending = []
            for k in range(2):
                appending.append(float(db[j][k]))
            X.append(appending)
            Y.append(float(symbolDict[db[j][2]]))

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = []
    for y in range(2):
        testSample.append(float(instance[y]))
    testSample.append(float(symbolDict[instance[2]]))
    
    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    class_predicted = clf.predict([testSample[:2]])[0]
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted != testSample[2]:
        error += 1

#print the error rate
#--> add your Python code here
print(error/10)





