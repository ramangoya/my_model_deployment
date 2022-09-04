import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def marks_prediction(marks):
    data=pd.read_csv("score.csv")
    x=data.iloc[:,-1]
    y=data["Scores"]
    X_train, X_test, y_train, y_test = train_test_split(x,y,train_size=0.8,random_state = 42)
    X_train = np.array(X_train).reshape(-1,1)
    X_test = np.array(X_test).reshape(-1,1)
    y_train = np.array(y_train).reshape(-1,1)
    y_test = np.array(y_test).reshape(-1,1)
    model=LinearRegression()
    model.fit(X_train,y_train)
    X_test=np.array(int(marks)).reshape(-1,1)
    pred=model.predict(X_test)
    return pred