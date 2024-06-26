# -*- coding: utf-8 -*-
"""Regression Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m9di3niaG534noI8CN4w_i38gzJkp23R
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import os


dataset = pd.read_csv('/content/drive/MyDrive/dataset/day.csv')
dataset.head()

dataset.info()

dataset.columns

sns.pairplot(dataset)

sns.distplot(dataset['cnt'])

numeric_dataset = dataset.select_dtypes(include=['number'])
sns.heatmap(numeric_dataset.corr(), annot=True, cmap='coolwarm', fmt=".2f")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = dataset[['instant', 'season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered']]
y= dataset['cnt']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4, random_state=101)
LR = LinearRegression()
LR.fit(X_train,  y_train)

print(LR.intercept_)

LR.coef_

X_train.columns

pd.DataFrame(LR.coef_, X.columns, columns=['Coeff'])

predictions = LR.predict(X_test)
predictions

y_test

plt.scatter(y_test,predictions)

sns.distplot(y_test-predictions)

from sklearn import metrics
metrics.mean_absolute_error(y_test, predictions)

metrics.mean_squared_error(y_test, predictions)

np.sqrt(metrics.mean_squared_error(y_test, predictions))