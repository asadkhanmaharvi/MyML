# -*- coding: utf-8 -*-
"""
Created on Sat May  5 04:42:42 2018

@author: Khan
"""
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score
df = pd.read_csv('SMSSpamCollection', delimiter='\t',header=None)
X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1],df[0])
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
for i, prediction in enumerate(predictions[:5]):
    print ('Prediction: %s. Message: %s' % (prediction, X_test_raw.iloc[i]))
#every time test data and training samples change
