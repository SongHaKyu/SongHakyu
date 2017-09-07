
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=15, max_depth=10, random_state=1)

model.fit(Final_train, y_train)

y_predict = model.predict(Final_test)

y_predict

np.array(y_test['Price'])

ytest_ypredict = np.array(y_test['Price']) - y_predict

###  Prediction Error
np.mean(   abs(ytest_ypredict) / np.array(y_test['Price'])   )   
