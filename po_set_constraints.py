"""
Requirements:
    Objective: Maximize the total return of the portfolio.
    Constraints: 
        - Select a certain number of stocks for the portfolio.
        - The cost of the purchased stocks cannot exceed a certain budget.
Given constants:
    stockcodes (list): List of stocks under consideration.
    average_returns (list): List of average monthly returns for each stock in stockcodes.
    daily_prices (list): List of current daily price for each stock in stockcodes.
    num_stocks_to_buy (int): Number of stocks to purchase.
    purchase_budget (float): Budget for purchase.
"""
# TODO: Import the required package.


# TODO: Initialize the nonlinear model object called model.


# 10 stocks to consider 
stockcodes=["T", "SFL", "PFE", "XOM", "MO", "VZ", "IBM", "TSLA", "GILD", "GE"]

# Average monthly returns
average_returns = [0.000286, 0.001169, -2.577749e-05, 0.000981, 0.000616, -0.000212, 0.000261, -0.002252, 0.000346, 0.001105]

# Prices
daily_prices = [27.286,5.9513,35.735,39.354,38.893,56.873,121.45,705.67,56.44,86.272]

# Number of stocks to purchase
num_stocks_to_buy = 2

# Set the budget for the purchase.
purchase_budget = 80.0

# TODO: Add the constants to the model object.
# Hint: Add the constant average_returns to the model object and name it returns.
# Hint: Add the constant daily_prices to the model object and name it prices.
# Hint: Add the constant purchase_budget to the model object and name it budget.


# TODO: Define the set variable and store it in selected_stocks. Use len() to get the total number of elements in the set.


# TODO: Set the objective function: maximize the total return of the portfolio.


# TODO: Add the constraint: The cost of the purchased stocks is less than or equal to the budget.