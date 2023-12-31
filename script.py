import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score #works
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('music.csv')
print(df)

X = df.drop(columns=['genre']);
y = df['genre']
X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

tree.export_graphviz(model, out_file='recommender.dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label='all')

output = model.predict(X_test);

score = accuracy_score(y_test, output)
print(score)