import cmd
import sys
import math
import os
from decimal import Decimal
import fractions
import statistics
import random


class_list = []

class CalcShell(cmd.Cmd):
    # Answer variable
    with open('ANS', 'r') as f:
        ans = f.read()
        ans = float(ans)
    intro = "Welcome to CLI Calculator. Type help to see help documentation"
    prompt = "(calculator)>>"

    def set_ans(self, var):
        '''Used to change the ANS variable'''
        self.ans = var
        with open('ANS', 'w') as f:
            f.write(str(var))

    def do_solve(self, arg):
        '''Solves any given mathematical statement'''
        string = str(arg)
        ansstring = string.replace('ans', str(self.ans))
        pistring = ansstring.replace('pi', str(math.pi))
        self.set_ans(float(eval(pistring)))
        print(str(eval(pistring)))
    def do_exit(self, arg):
        '''Exits the program'''
        sys.exit()
    def do_ans(self, arg):
        '''Prints the ANS variable'''
        print("ANS currently is: " + str(self.ans))
    def do_clearans(self, arg):
        '''Clears the ANS variable'''
        self.set_ans(0)
        print("ANS Has been cleared")
    def do_pi(self, arg):
        '''Displays the first 16 digits of PI'''
        print(str(math.pi))
    def do_clear(self, arg):
        '''Clears the terminal'''
        os.system('cls')
    def do_save(self, arg):
        '''Saves the current ANS variable to a file specified in the parameters'''
        with open(arg + ".txt", 'w') as f:
            f.write(str(self.ans))
            print("Written to: " + arg + ".txt")
    def do_fractodec(self, arg):
        '''Converts a fraction to a decimal'''
        fraction = arg.split('/')
        a = float(fraction[0]) / float(fraction[1])
        print(a)
    def do_fractopct(self, arg):
        '''Converts a fraction to a percentage'''
        fraction = arg.split('/')
        a = float(fraction[0]) / float(fraction[1])
        a = str(a * 100)
        print(a + '%')
    def do_dectofrac(self, arg):
        '''Converts a decimal/float to its fractional value'''
        decimal = Decimal(arg)
        print(fractions.Fraction(decimal))
    def do_pythagoras(self, arg):
        '''Takes two numbers and finds the hypotenuse'''
        args = arg.split()
        a = float(args[0]) ** 2
        b = float(args[1]) ** 2
        c = a + b
        c = math.sqrt(c)
        print(c)
        self.set_ans(c)
    def do_invpyth(self, arg):
        '''Solves a right triangle with a hypotenuse and one side similar to the pythagoras cmd. HYPOTENUSE FIRST'''
        args = arg.split()
        c = float(args[0]) ** 2
        b = float(args[1]) ** 2
        a = c - b
        a = math.sqrt(a)
        print(a)
        self.set_ans(a)
    def do_circumference(self, arg):
            '''Takes in the diameter of a circle at returns it's circumference'''
            a = float(arg) * math.pi
            print(a)
            self.set_ans(a)
    def do_circulararea(self, arg):
        '''Finds the area of a circle based on a radius/diamter divided by 2'''
        a = float(arg) ** 2
        a = a * math.pi
        print(a)
        self.set_ans(a)
    def do_average(self, arg):
        '''Finds the average of a list of numbers: average 1,2,3,4,5,6'''
        list = arg.split(',')
        list_of_floats = []

        for item in list:
            list_of_floats.append(float(item))
        a = statistics.mean(list_of_floats)
        print(a)
        self.set_ans(a)
    def do_median(self, arg):
        '''Finds the median of a list of numbers: median 1,2,3,4,5,6'''
        list = arg.split(',')
        list_of_floats = []

        for item in list:
            list_of_floats.append(float(item))
        a = statistics.median(list_of_floats)
        print(a)
        self.set_ans(a)
    def do_mode(self, arg):
        '''Finds the mode of a list of numbers: median 1,2,3,4,5,6'''
        list = arg.split(',')
        list_of_floats = []

        for item in list:
            list_of_floats.append(float(item))
        a = statistics.mode(list_of_floats)
        print(a)
        self.set_ans(a)
    def do_randomfloat(self, arg):
        '''Returns a random float in between two given values'''
        split = arg.split()
        a = random.randrange(split[0], split[1])
        print(a)
        self.set_ans
    def do_random(self, arg):
        '''Returns a random integer in between two given values'''
        split = arg.split()
        a = random.randint(split[0], split[1])
        print(a)
        self.set_ans
    # Aliases
    def do_pyth(self, arg):
        '''Alias for pythagoras function'''
        self.do_pythagoras(arg)
    def do_cls(self, arg):
        '''Alias for clear'''
        self.do_clear(arg)
    def do_avg(self, arg):
        '''Alias for average command'''
        self.do_average(arg)
if __name__ == '__main__':
    shell = CalcShell()
    os.system('title PyCalc - Version 1.00')
    os.system('.\\config.bat')
    shell.cmdloop()