import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# matplotlib.use('TkAgg')

# import glass.csv as DataFrame
data = pd.read_csv("glass.csv", names=["Id", "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe", "Glass type"],
                   index_col=0)

''' Instructions
1. split the data into 70% training and 30% testing data
    - use Na, Mg, Al, Si, K, Ca, Ba, and Fe (i.e. all columns except Glass type) as the input features.
    - use Glass type as the target attribute.

2. plot the accuracy of knn classifiers for all odd value of k between 3 to 100, i.e. k = 3, 5, 7, ..., 100. This is achieved by fulfilling the following tasks:
    i. create a loop to 
      A. fit the training data into knn classifiers with respective k.
      B. calculate the accuracy of applying the knn classifier on the testing data.
      C. print out the accuracy for each k.

    ii. plot a line graph with the y-axis being the accuracy for the respective k and x-axis being the value of k. You DO NOT need to save the graph.
'''

# start your code after this line

glass = {
    'attributes': data.drop('Glass type', axis=1),
    'target': pd.DataFrame(data, columns=['Glass type']),
    'targetNames': list(data.columns)
}

x, xT, y, yT = train_test_split(glass['attributes'], glass['target'], test_size=0.3, random_state=1)

glass['train'] = {
    'attributes': x,
    'target': y
}
glass['test'] = {
    'attributes': xT,
    'target': yT
}

k = []
accuracies = []

for i in range(3, 101):
    if i % 2 == 1:
        knc = KNeighborsClassifier(i)
        cols = glass['attributes'].columns.tolist()
        x = glass['train']['attributes'][cols]
        y = glass['train']['target'].values.ravel()
        knc.fit(x, y)
        xT = glass['test']['attributes'][cols]
        yT = glass['test']['target'].values.ravel()
        y_predict = knc.predict(xT)

        # Output
        print(f'k = {i}')
        print(pd.DataFrame(list(zip(yT, y_predict)), columns=['target', 'predicted']))
        print(f'Accuracy: {knc.score(xT, yT):.4f}')

        k.append(i)
        accuracies.append(knc.score(xT, yT))

plt.figure(figsize=[10, 5])
plt.title('k vs accuracy')

plt.ylim(ymin=0)

plt.scatter(k, accuracies)
plt.xlabel('k')
plt.ylabel('Accuracy')

# plt.waitforbuttonpress()
