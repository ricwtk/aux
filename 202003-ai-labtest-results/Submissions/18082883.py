# Student ID: 18082883
import pandas as pd

# import glass.csv as DataFrame
data = pd.read_csv("glass.csv", names=["Id", "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe", "Glass type"], index_col=0)

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
from sklearn.model_selection import train_test_split

glass = pd.DataFrame(data)
input_features=['Na','Mg','Al','Si','K','Ca','Ba','Fe']
x_train, x_test, y_train, y_test = train_test_split(glass[input_features], glass["Glass type"], test_size=0.3, random_state=1)

from sklearn.neighbors import KNeighborsClassifier

k_list = []
accuracy_list = []

for k in range(3, 101):
    if(k % 2) != 0:
        k_list.append(k)
        knc = KNeighborsClassifier(k)
        knc.fit(x_train, y_train)
        accuracy = knc.score(x_test, y_test)
        print(k)
        print(accuracy)
        print("\n")
        accuracy_list.append(accuracy)

import matplotlib.pyplot as pt
pt.figure()
pt.scatter(k_list, accuracy_list)
pt.xlabel('Value of k')
pt.ylabel('Accuracy')
pt.title('Comparison of Accuracy for different k')
#pt.show()
