#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]

#########################################################
from sklearn.svm import SVC
#Create SVM Calssifier
svm_clf = SVC(C = 10000)
#Fit data into the classifier to create model
svm_clf.fit(features_train, labels_train)
#Pass Testing Features to Get A Prediction Out of The Classifier
pred = svm_clf.predict(features_test)

from sklearn.metrics import accuracy_score
#Get Accuracy of The Prediction By Comparing With the Testing Labels
acc= accuracy_score(pred, labels_test)

print(acc)
#########################################################
#Accuracy = 0.9908987485779295


