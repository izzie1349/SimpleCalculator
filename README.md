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
