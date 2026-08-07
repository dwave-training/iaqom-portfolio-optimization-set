[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-portfolio-optimization-set?quickstart=1)
  
# Portfolio Optimization with Stride<sup>TM</sup> Hybrid Solver using a Set Variable

For the portfolio optimzation problem, convert the mathematical formulation into a model in Python code. Instead of using binary variables to represent the decision variable, use a set variable to code the problem so that it is compatible for submission to the Stride hybrid solver.

The objective is to maximimze the total return of the portfolio. The decision variable is which stocks are included in the portfolio. There are two constraints: a certain number of stocks must be selected for the portfolio, and the available budget for purchasing stocks cannot be exceeded.

Build the nonlinear model then define the objective function and add the constraints.

In this exercise, the average monthly returns and the daily closing prices for 10 stocks are provided. The stocks considered in this exercise are "T" (AT&T), "SFL" (FSL), "PFE" (Pfizer), "XOM" (Exxon Mobil), "MO" (Altria Group), "VZ" (Verizon Communications), "IBM" (IBM), "TSLA" (Tesla), "GILD" (Gilead Sciences), and "GE" (General Electric).

## Exercise 1

In the first exercise, build a basic portfolio of two stocks to maximize the total return. Add a constraint that the cost of the purchased stocks cannot exceed a certain budget. Formulate the problem so that it is compatible for submission to the Stride Hybrid solver, but do not yet submit it to the solver.

Open the code file `po_set_constraints.py`.

   1. Create a nonlinear model object called `model` and import the required package.

   2. Add the constants to the model object.
      - Add `average_returns` to the model object and name it `returns`.
      - Add `daily_prices` to the model object and name it `prices`.
      - Add `purchase_budget` to the model object and name it `budget`.
   
   3. Define the set decision variable and store it in `selected_stocks`. Use `len()` to determine the total number of elements in the set.
   The constraint on the number of selected stocks can be treated as implicit. Ensuring that exactly two stocks are selected is enforced by the structure of the set decision variable, which restricts its size. Therefore, be sure to specify this using the `min_size` and `max_size` parameters.

   4. Define the objective function to maximize the total return of the portfolio.

   ```math
   \min \left[-
   {returns[selected\_stocks]}.sum()
   \right]
   ```

   5. Add the constraint that the cost of the purchased stocks cannot exceed a certain budget.
   ```math
   {prices[selected\_stocks]}.sum() \leq budget
   ```

## Exercise 2

In exercise 2, you will test the code after providing an initial state.

Start with the work you did in exercise 1. Create the model object, add the constants to the model, define the decision variable, then set the objective function and add the constraint. Finally, provide an initial state.

Open the code file `po_set_initial_state.py`.

   1. Repeat steps 1 to 5 of exercise 1. You may copy all the work you submitted in the code file `po_set_constraints.py`.
   
   2. Lock the model using a context manager. Include the following steps in the block:

      a. Define the number of states. In this case, only one state is being tested.
   
      b. Provide the following initial state `[3,4]`. This set is chosen randomly and satisfies the constraints. Remember to use the `set_state()` method to assign the specifcied state to its index.

      c. Return the initial state for the set variable symbol and store it in `stocks_state`.

      d. Return the objective value of the initial state and store it in `objective_value`.

## Exercise 3

For exercise 3, submit the problem to the Stride hybrid solver to obtain the best solution.

Start with the work you did in exercise 1. Create the model object, add the constants to the model, define the decision variable, then set the objective function and add the constraint. Then, submit the problem to the Stride solver.

Open the code file `po_set_submit.py`.

   1. Repeat steps 1 to 5 of exercise 1. You may copy all the work you submitted in the code file `po_set_constraints.py`.
   
   2. Lock the model explicitly to prevent further changes.

   3. Instantiate the nonlinear sampler and name it `sampler`.
   
   4. Submit the nonlinear model to the nonlinear sampler. Give this problem a label on your Leap dashboard by using the `label` parameter. Use the label 'Portfolio_Set'. Note that this label is case sensitive and uses an underscore.

   5. Return the best solution for the set variable symbol and store it in `stocks_state`.

   6. Return the objective value of the best solution and store it in `objective_value`.