import numpy as np
import matplotlib.pyplot as plt

from data import get_data, inspect_data, split_data

data = get_data()
inspect_data(data)

train_data, test_data = split_data(data)

# Simple Linear Regression
# predict MPG (y, dependent variable) using Weight (x, independent variable) using closed-form solution
# y = theta_0 + theta_1 * x - we want to find theta_0 and theta_1 parameters that minimize the prediction error

# We can calculate the error using MSE metric:
# MSE = SUM (from i=1 to n) (actual_output - predicted_output) ** 2

# get the columns
y_train = train_data['MPG'].to_numpy()
x_train = train_data['Weight'].to_numpy()

y_test = test_data['MPG'].to_numpy()
x_test = test_data['Weight'].to_numpy()

# TODO: calculate closed-form solution
theta_best = [0, 0]

matrix = np.vstack([np.ones(len(x_train)), x_train]).T
theta_best = np.linalg.inv(matrix.T @ matrix) @ (matrix.T @ y_train)

# TODO: calculate error
mse_theta = np.mean(((matrix @ theta_best)-y_train)**2)
matrix_test = np.vstack([np.ones(len(x_test)), x_test]).T
mse_theta_test = np.mean(((matrix_test @ theta_best)-y_test)**2)
print("Train mse: ", mse_theta)
print("Test mse: ", mse_theta_test)


# plot the regression line
x = np.linspace(min(x_test), max(x_test), 100)
y = float(theta_best[0]) + float(theta_best[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

# TODO: standardization
x_standarized = (x_train - np.mean(x_train))/np.std(x_train)
y_standarized = (y_train - np.mean(y_train))/np.std(y_train)
y_standarized = np.expand_dims(y_standarized, axis = 1)
# TODO: calculate theta using Batch Gradient Descent
diff = 1
lp = 0.1
matrix = np.vstack([np.ones(len(x_standarized)), x_standarized]).T
theta = np.array([np.random.random(), np.random.random()])
theta = np.expand_dims(theta, axis = 1)
last_mse = 0
mse = mse_theta
while (diff != 0):
    gradient_mse = (2 / len(x_standarized)) * (matrix.T @ (matrix @ theta - y_standarized))
    theta = theta - lp * (gradient_mse)
    mse = np.mean(((matrix @ theta)-y_standarized)**2)
    diff = last_mse - mse
    last_mse = mse

yStd = np.std(y_train)
xStd = np.std(x_train)
yMean = np.mean(y_train)
xMean = np.mean(x_train)

scaled_theta = theta.copy()
scaled_theta[1] = scaled_theta[1] * yStd/ xStd
scaled_theta[0] = yMean - scaled_theta[1] * xMean
scaled_theta = scaled_theta.reshape(-1)
print(scaled_theta)
# TODO: calculate error
matrix_test = np.vstack([np.ones(len(x_test)), x_test]).T
mse_theta_test = np.mean(((matrix_test @ scaled_theta)-y_test)**2)
matrix = np.vstack([np.ones(len(x_train)), x_train]).T
mse_theta = np.mean(((matrix @ scaled_theta)-y_train)**2)

print("Train Error: ", mse_theta)
print("Test Error: ", mse_theta_test)

# plot the regression line
x = np.linspace(min(x_test), max(x_test), 100)
y = float(scaled_theta[0]) + float(scaled_theta[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()