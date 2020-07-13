import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
# import glass.csv as DataFrame
data = pd.read_csv("glass.csv", names=["Id", "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe", "Glass type"], index_col=0)
data=pd.DataFrame(data)
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
input_features=['Na','Mg','Al','Si','K','Ca','Ba','Fe','RI']
X_train, X_test, y_train, y_test = train_test_split(data[input_features], data['Glass type'], test_size=0.3, random_state=1)

odd_num=[]
acc_list=[]
for i in range(3,101):
   if (i%2) !=0:
       odd_num.append(i)
       knc=KNeighborsClassifier(i)
       knc.fit(X_train,y_train)
       accuracy=knc.score(X_test,y_test)
       print(f'Accuracy: {knc.score(X_test,y_test):.4f}')
       acc_list.append(accuracy)
       val_predictions = knc.predict(X_test)
       print(mean_absolute_error(y_test, val_predictions))

plt.ion()
plt.figure()
plt.plot(odd_num,acc_list)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("the accuracy for the respective k and x-axis being the value of k")


