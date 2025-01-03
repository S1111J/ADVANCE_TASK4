X = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

def mean(values):
    """Calculate the mean of a list of values."""
    return sum(values) / len(values)

def covariance(X, mean_x, y, mean_y):
    """Calculate the covariance between X and y."""
    covar = sum((x - mean_x) * (y_i - mean_y) for x, y_i in zip(X, y))
    return covar

def variance(values, mean):
    """Calculate the variance of a list of values."""
    return sum((x - mean) ** 2 for x in values)

def coefficients(X, y):
    """Calculate the slope (b1) and intercept (b0) of the linear regression line."""
    mean_x = mean(X)
    mean_y = mean(y)
    
    b1 = covariance(X, mean_x, y, mean_y) / variance(X, mean_x)
    b0 = mean_y - b1 * mean_x
    
    return b0, b1

def predict(b0, b1, X):
    """Make predictions using the linear regression model."""
    return [b0 + b1 * x for x in X]

b0, b1 = coefficients(X, y)

print(f"Intercept (b0): {b0}")
print(f"Slope (b1): {b1}")

predictions = predict(b0, b1, X)

print("Predictions:", predictions)
