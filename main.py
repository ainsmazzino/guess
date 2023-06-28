import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music = pd.read_csv("C:\CODING\machinelearning\music.csv")
music.describe
X = music.drop(columns=['genre'])
y = music['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

model1 = DecisionTreeClassifier()
model1.fit(X.values, y)

predictions = model.predict(X_test)


#n=input("enter your age :")
#m=input("enter your gender :")
pred = model1.predict([[20, 1]])

score = accuracy_score(y_test, predictions)

print(pred)




