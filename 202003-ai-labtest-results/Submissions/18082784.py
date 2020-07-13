import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from math import fabs, inf
import sys
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

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
dt = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.DataFrame(data.target, columns=['Glass'])

X_train, X_test, y_train, y_test = train_test_split(dt, y, test_size=0.2)

def model(x, m, c):
  return m*x + c

def cost(y, yh):
  return ((y-yh)**2).mean()

def derivatives(x, y, yh):
  return {
    'm': ((y-yh)*x).mean()*-2,
    'c': (y-yh).mean()*-2
  }

learningrate = 0.1
m = []
c = []
J = []
m.append(0)
c.append(0)
J.append(cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))))


J_min = 0.01
del_J_min = 0.0001
max_iter = 10000

plt.ion()

plt.scatter(X_train['glass'], y_train['target'], color='red')
plt.title('Training data')
plt.xlabel('Glass Type')
line = None

def getdelJ():
  if len(J) > 1:
    return fabs(J[-1] - J[-2])/J[-1]
  else:
    return inf

while J[-1] > J_min and getdelJ() > del_J_min and len(J) < max_iter:
  der = derivatives(X_train['bmi'], y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1])))
  m.append(m[-1] - learningrate * der['m'])
  c.append(c[-1] - learningrate * der['c'])
  J.append(cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))))

  print('.', end='')
  sys.stdout.flush()

  if line:
    line[0].remove()
  line = plt.plot(X_train['bmi'], X_train['glass'].apply(lambda x: model(x, m[-1], c[-1])), '-', color='green')
  plt.pause(0.001)

y_train_pred = X_train['glass'].apply(lambda x: model(x, m[-1], c[-1]))
y_test_pred = X_test['glass'].apply(lambda x: model(x, m[-1], c[-1]))
print('\nAlgorithm terminated with')
print(f'  {len(J)} iterations')
print(f'  m {m[-1]}')
print(f'  c {c[-1]}')
print(f'  training cost {J[-1]}')
testcost = cost(y_test['target'], y_test_pred)
print(f'  testing cost {testcost}')

plt.figure()
plt.scatter(X_test['glass'], y_test['target'], color='red')
plt.plot(X_test['glass'], y_test_pred, '-', color='green')
plt.title('Testing data')
