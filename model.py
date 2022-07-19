import csv
import sklearn
import joblib
from sklearn.neighbors import KNeighborsClassifier

# Makes the data compatible with the sklearn model because it is picky
def load_data(data):
    evidence = []
    labels = []

    with open(data) as data:
        dreader = csv.reader(data)
        evidence = list(dreader)
    evidence.pop(0)

    for x in range(len(evidence)):
       labels.append(evidence[x].pop(0))
       evidence[x] = list(map(int,evidence[x]))
       
    return evidence,labels
    
# i didnt know what joblib was before this but apparently it hold models!

evidence, labels = load_data('blocks.csv')

# Train model and make predictions
model = KNeighborsClassifier(n_neighbors=1)
model.fit(evidence,labels)
print(model.predict([[125,154,0]]))

joblib.dump(model,'model.joblib')
