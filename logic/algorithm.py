import os
import joblib
import numpy as np
logisticRegression = joblib.load(os.getcwd()+'\logic\RandomForest.joblib')

def getResult(li:list):

  features = np.array([li])

  pred = logisticRegression.predict(features)

  return pred[0]