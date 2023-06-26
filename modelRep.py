import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('seaborn-darkgrid')

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is: {m}")

n = len(x_train)
print(f"Number of training examples is: {n}")

i = 0 
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# plt.scatter(x_train, y_train, marker = 'x', c= 'r')
# plt.title("Housing prices")
# plt.ylabel('Print in 1000s of dollars')
# plt.xlabel('Size in 1000 sqft')
# plt.show()

w = 200
b = 100 
print(f"w: {w}")
print(f"b: {b}")

def computer_model_output (x, w, b):
# Computes the prediction of a linear model 
# Args: x (ndarray (m,)): Data, m examples 
# w, b (scalar): model parameters 
# Returns 
# y (ndarray (m, )): target values 
    m = x_train.shape[0]
    f_wb = np.zeros(m)
    for i in range(m): 
        f_wb[i] = w*x_train[i] + b
    return f_wb

tmp_f_wb = computer_model_output(x_train, w, b)

plt.plot(x_train, tmp_f_wb, c='b', label = 'Our Prediction')
plt.scatter(x_train, y_train, marker = 'x', c = 'r', label = 'Actual values')

plt.title("Housing Prices")
plt.ylabel("Price in 1000s of dollars")
plt.xlabel('Size in 1000 of sqft')
plt.legend()
plt.show()     
x_i = 1.2
cost_1200sqft = w * x_i + b    

print(f"${cost_1200sqft:.0f} thousand dollars")