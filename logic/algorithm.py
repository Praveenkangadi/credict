import os
import joblib
import numpy as np
RandomForest = joblib.load(os.getcwd()+r'/logic/RandomForest.joblib')

def getResult(li:list):

  features = np.array([li])

  pred = RandomForest.predict(features)

  return pred[0]