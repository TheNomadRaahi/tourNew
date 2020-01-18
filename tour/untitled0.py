# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:44:01 2019

@author: Asus
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data=pd.read_csv("C:/Users/Asus/Downloads/50_Startups.csv")
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x=pd.get_dummies(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
y_predict=lr.predict(x_test)

import statsmodels.formula.api as sm 
x = np.append(arr = np.ones((50, 1)).astype(int),values = x, axis = 1) 
''' choose a Significance level usually 0.05, if p>0.05 
for the highest values parameter, remove that value ''' 
x_opt = x[:, [0, 1, 2, 3, 4, 5]] 
ols = sm.OLS(endog = y, exog = x_opt).fit() 
ols.summary() 
x_opt = x[:, [0, 1, 2, 3, 5]] 
ols = sm.OLS(endog = y, exog = x_opt).fit() 
ols.summary() 
x_opt = x[:, [0, 1, 2, 3]] 
ols = sm.OLS(endog = y, exog = x_opt).fit() 
ols.summary() 
x_opt = x[:, [0, 1, 3]] 
ols = sm.OLS(endog = y, exog = x_opt).fit() 
ols.summary() 
x_opt = x[:, [0, 1]] 
ols = sm.OLS(endog = y, exog = x_opt).fit() 
ols.summary() 