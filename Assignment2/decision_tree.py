#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries

def transform(csvList, distance):
    storage = []
    for i in range (0, len(csvList)):
        storage.append([])

    for i in range(0,distance):
        count = 1
        for j in range(0,len(csvList)):
            if csvList[j][i] not in symbolDict:
                symbolDict[csvList[j][i]] = count
                count += 1
            storage[j].append(symbolDict.get(csvList[j][i]))

    return storage


from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    symbolDict = {}
    symbolDict.clear()
    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    X = transform(dbTraining, 4)

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    for x in dbTraining:
        if x[4] == "Yes":
            Y.append(1)
        else:
            Y.append(0)

    #loop your training and test tasks 10 times here
    currentLowest = 2
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for i, row in enumerate(reader):
                    if i > 0: #skipping the header
                        dbTest.append (row)

        dbTest = transform(dbTest, 5)
        for x in dbTest:
            x[4] -= 1
        accurateGuess = 0
        for data in dbTest:
            #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            class_predicted = clf.predict([data[:4]])[0]
            
            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if class_predicted == data[4]:
                accurateGuess += 1
        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
        accuracy = accurateGuess / (len(dbTest)-1)
        currentLowest = min(accuracy, currentLowest)
    #print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("Final accuracy when training on " + ds + ": " + str(currentLowest))