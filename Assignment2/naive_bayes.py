#-------------------------------------------------------------------------
# AUTHOR: Daniel Yoon
# FILENAME: naive_bayes.py
# SPECIFICATION: fufills assignment requirements
# FOR: CS 4210- Assignment #2
# TIME SPENT: 20 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
#reading the training data
#--> add your Python code here
dbTraining = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTraining.append (row)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
symbolDict = {
    'Yes' : 1,
    'No' : 2
}
X = []

for i in range(len(dbTraining)):
    X.append([])

for i in range(1,5):
    count = 1
    for x in range(len(dbTraining)):
        if dbTraining[x][i] not in symbolDict:
            symbolDict[dbTraining[x][i]] = count
            count += 1
        X[x].append(symbolDict.get(dbTraining[x][i]))

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []

for x in dbTraining:
    Y.append(symbolDict.get(x[5]))

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
dataset = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dataset.append (row)

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for row in dataset:
    predicted = list(clf.predict_proba([[symbolDict.get(row[1]), symbolDict.get(row[2]), symbolDict.get(row[3]), symbolDict.get(row[4])]])[0])
    maxValue = max(predicted)
    if(maxValue >= 0.75):
        if(predicted.index(maxValue) == 0):
            row[5] = 'Yes'
        else:
            row[5] = 'No'
        row.append(maxValue)
        print(str(row[0]).ljust(15) + str(row[1]).ljust(15) + str(row[2]).ljust(15) + str(row[3]).ljust(15) + str(row[4]).ljust(15) + str(row[5]).ljust(15) + str(row[6]).ljust(15))
