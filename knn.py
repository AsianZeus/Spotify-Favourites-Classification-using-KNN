import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import pickle
excel_file = 'C://Users//akroc//Desktop//newtraindata.xlsx'
songs = pd.read_excel(excel_file)
print(songs.head())

X = songs.iloc[:,2:12 :].values
print(X)
y = songs.iloc[:, 15].values
print(y)

from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 6)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(classifier.score(X,y))
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)
result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)
result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)
pickle.dump(classifier,open("C://Users//akroc//Desktop//finalmodelnew.sav",'wb'))

excel_file = 'C://Users//akroc//Desktop//trainingdatanewest.xlsx'
songs = pd.read_excel(excel_file)
X = songs.iloc[:,2:12 :].values
X_test = scaler.transform(X)
loaded_model = pickle.load(open("C://Users//akroc//Desktop//finalmodelnew.sav", 'rb'))
result = loaded_model.predict(X_test)
name=songs.iloc[:,1].values
for n in range(len(name)):
    print(name[n],result[n])