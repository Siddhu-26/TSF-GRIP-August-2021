import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Storing the dataset
given = pd.read_csv('E:\TSF\T1- Percentage of student using study hours\data.csv')

# Storing them in 2 variables
x = np.array(given[given.columns[0]]).reshape(-1,1)
y = np.array(given[given.columns[1]])


model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)


# Plotting the graph with Regression Line
plt.scatter(x, y)
plt.plot(x, y_pred)
plt.show()

# Predicting
sas = np.array(9.25)
sol = model.predict(sas.reshape(-1,1))

#Printing the solution
print(sol)