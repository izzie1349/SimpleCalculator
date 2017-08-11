# SimpleCalculator
A calculator that takes in two operands and operation, then performs the operation on the operand

#### Using SimpleCalculator

First clone the project
~~~
git clone https://github.com/izzie1349/SimpleCalculator.git
~~~

Run the app
~~~
python calculator.py
~~~

You will be asked to enter two operands and an operation to be performed on
them. For example: <5> and <2>, and <+>, will return <7>. If a particular
operation requires only one operand, it will neglect the second operand
entered. For example: 36 and 2, and s (for square root) will return the
the square root of 36.

Then, you will be asked if you would like to continue using the app.
Entering 'Y' will bring you back the initial state of the app, and entering 'N'
will quit the app.


Run the tests
~~~
python test_calculator.py
~~~
This will create an output file called 'test_out', where execution timestamp, testcase name, and testcase result will be logged


#### Test Strategies

* Function Testing
    1. Identify things that the Calculator can do (functions and subfunctions).
    2. Determine how you’d know if a function was capable of
    working.
    3. Test each function, one at a time.
    4. See that each function does what it’s supposed to do and
    not what it isn’t supposed to do.

* Group Testing
    1. Identify categories and roles of users. For example, an accountant or          scientist may have different flows and use of calculators
    2. Determine what each category of user will do (use cases), how
    they will do it, and what they value.
    3. Get real user data, or bring real users in to test. Bringing in different      departments works here!
    4. Otherwise, systematically simulate a user (be careful—it’s
    easy to think you’re like a user even when you’re not).
    5. Powerful user testing is that which involves a variety of users
    and user roles, not just one.

* Automatic Checking
    1. Look for or develop tools that can perform a lot of actions and
    check a lot things.
    2. Consider tools that partially automate test coverage.
    3. Consider tools that partially automate oracles.
    4. Consider automatic change detectors.
    5. Consider automatic test data generators.
    6. Consider tools that make human testing more powerful
