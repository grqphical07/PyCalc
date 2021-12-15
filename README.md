# CLI Calculator

A simple scientfic CLI Calculator with history, ANS variable and more.

Written in 100 percent Python!

Start by using the solve command to solve a given equation

***
## ANS Variable
The ANS Variable is the last answer to an equation run with any of the functions similar to Ans on a scientific calculator

***

## Supports these operations:
    - Addition: +
    - Subtraction: -
    - Multiplication: *
    - Division: /
    - Modulus/Remainder: %
    - Exponentation: **
        - Example: 5 ** 2 = 25, 2 ** 3 = 8
    - Floor Division: //
        - Example 7 // 2 = 3, 5 // 2 = 2
---
## Functions:
    - Pythagoras Theorem (pyth a b)
    - Inverse Pythagoras (invpyth c b)
    - pi prints out the first 16 digits of pi and can be used in equations with the solve command
    - save: Saves the ANS variable to a file
        - Example: Saves ANS to a file called test.txt: save test
    - fractodec: converts a given fraction to a decimal
      - Example: fractodec 1/4 = 0.25
    - fractopct: Converts a fraction to a percent
    - dectofrac: Converts a decimal to its fractional form
    - circulararea: Finds the area of a circle given a radius
    - circumference: Finds the circumference of a circle given a diameter
    - average/avg: Finds the average of a list of numbers
      - Example: average 1,2,3,4,5,6 = 3.5
    - median: Finds the median of a list of numbers
    - mode: Finds the mode of a list of numbers
    - randomfloat: Generates a random float between two specified numbers
    - random: Generates a random integer between two specified numbers
## Configuration
Use config.bat to configure things such as terminal color, title etc