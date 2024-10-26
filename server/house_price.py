# comment this code due to some error while deploying so you need to uncoment this code to generate model
# # Import libraries
# from sklearn.linear_model import LinearRegression
# import joblib  # For saving the model
# import numpy as np

# # Sample data (features: [number of rooms, size (sq. ft), age of house])
# X = np.array([[3, 1500, 20], [4, 2500, 15], [2, 800, 30], [5, 3000, 10]])
# y = np.array([200000, 300000, 120000, 400000])  # Prices in dollars

# # Train the model
# model = LinearRegression()
# model.fit(X, y)

# # Save the model
# joblib.dump(model, "house_price_model.pkl")
