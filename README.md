[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-portfolio-optimization-set?quickstart=1)
  
# Portfolio Optimization With the Stride<sup>TM</sup> Hybrid Solver Using a Set Variable

For the portfolio optimization problem, convert the mathematical formulation into a model in Python. Use a set to represent the decision variable and code the problem so that it is compatible for submission to the Stride hybrid solver.

The objective is to maximimze the total return of the portfolio. The decision variable represents the stocks that are included in the portfolio. There are two constraints: a certain number of stocks must be selected for the portfolio, and the available budget for purchasing stocks cannot be exceeded.

Build the nonlinear model, define the objective function, and add the constraints.

In this exercise, the average monthly returns and the daily closing prices for 10 stocks are provided. The stocks considered in this exercise are "T" (AT&T), "SFL" (FSL), "PFE" (Pfizer), "XOM" (Exxon Mobil), "MO" (Altria Group), "VZ" (Verizon Communications), "IBM" (IBM), "TSLA" (Tesla), "GILD" (Gilead Sciences), and "GE" (General Electric).

## Exercise 1

In the first exercise, build a basic portfolio of two stocks to maximize the total return. Add a constraint that the cost of the purchased stocks cannot exceed a certain budget. Formulate the problem so that it is compatible for submission to the Stride Hybrid solver, but do not yet submit it to the solver.

Open `po_set_constraints.py` and do the following:

   1. Import the relevant package(s).

   2. Create a nonlinear model object called `model`.

   3. Add the following constants to the model object:
      - `average_returns` and name it `returns`.
      - `daily_prices` and name it `prices`.
      - `purchase_budget` and name it `budget`.
   
   4. Define the set decision variable and store it in `selected_stocks`. Use `len()` to determine the total number of elements in the set.
   The constraint on the number of selected stocks can be treated as implicit. To ensure that exactly two stocks are selected, restrict the size of the set decision variable by using the `min_size` and `max_size` parameters.

   5. Define the objective function to maximize the total return of the portfolio as follows:

   ```math
   \min \left[-
   {returns[selected\_stocks]}.sum()
   \right]
   ```

   6. Add the constraint that the cost of the purchased stocks cannot exceed a certain budget as follows:
   ```math
   {prices[selected\_stocks]}.sum() \leq budget
   ```

## Exercise 2

In exercise 2, test the code after providing an initial state.

Start with the work completed in exercise 1. Create the model object, add the constants to the model, define the decision variable, set the objective function, and add the constraint. Finally, provide an initial state.

Open `po_set_initial_state.py`.

   1. Repeat steps 1 to 6 of exercise 1. You may copy all the work you submitted in `po_set_constraints.py`.
   
   2. Lock the model using a context manager. Include the following steps in the block:

      a. Define the number of states. In this case, only one state is being tested.
   
      b. Provide the following initial state `[3, 4]`. This set is chosen randomly and satisfies the constraints. Remember to use the `set_state()` method to assign the specified state to its index.

      c. Return the initial state for the set variable symbol and store it in `stocks_state`.

      d. Return the objective value of the initial state and store it in `objective_value`.

## Exercise 3

For exercise 3, to obtain the best solution, submit the problem to the Stride hybrid solver.

Start with the work completed in exercise 1. Create the model object, add the constants to the model, define the decision variable, set the objective function, and add the constraint. Then, submit the problem to the Stride solver.

Open `po_set_submit.py`.

   1. Repeat steps 1 to 6 of exercise 1. You may copy your previous work from `po_set_constraints.py`.
   
   2. Lock the model explicitly to prevent further changes.

   3. Instantiate the nonlinear sampler and name it `sampler`.
   
   4. Submit the nonlinear model to the Stride hybrid solver. Label your problem "Portfolio_Set" using the `label` parameter. Note that this label is case-sensitive and uses an underscore. When you submit your problem, this label will display in your Leap dashboard.

   5. Return the best solution for the set variable symbol and store it in `stocks_state`.

   6. Return the objective value of the best solution and store it in `objective_value`.
   