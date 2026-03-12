# Basic model, will use last n prices to predict the next price. 

import yfinance as yf
from main import get_nifty50_data

class Model:
    def __init__(self, n):
        self.n = n
        self.w = [0.0] * n 
        self.prev = 99999999999
        self.lr = 0.0000000001

    def predict(self, x):
        y = 0.0
        for i in range(self.n):
                y += self.w[i] * x[i]
        return y
    
    def train(self, x, y_true):
        y_pred = self.predict(x)
        error = y_pred - y_true
        for i in range(self.n):
             self.w[i] -= self.lr * error * x[i]
        if abs(error) > abs(self.prev):
             self.lr *= 0.1
        self.prev = error

a = get_nifty50_data()["Close"].values

model = Model(n=5)

for i in range(5, 400):
    x = a[i-5:i]
    y_true = a[i]
    model.train(x, y_true)

#test time
for i in range(405, 410):
    x = a[i-5:i]
    y_true = a[i]
    y_pred = model.predict(x)
    print(f"Predicted: {y_pred}, Actual: {y_true}", f"Error: {y_pred - y_true}")

print("Yeah this model is fucked")



