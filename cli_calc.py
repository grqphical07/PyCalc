import cmd
import sys
import math
import os

class CalcShell(cmd.Cmd):
    # Answer variable
    ans = 0
    intro = "Welcome to CLI Calculator. Type help to see help documentation"
    prompt = "(calculator)>>"

    def set_ans(self, var):
        self.ans = float(var)

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
    def do_manual(self, arg):
        '''Prints the README file'''
        with open('README_text.txt', 'r') as f:
            print(f.read())
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
    # Aliases
    def do_pyth(self, arg):
        '''Alias for pythagoras function'''
        self.do_pythagoras(arg)
    def do_cls(self, arg):
        '''Alias for clear'''
        self.do_clear(arg)


if __name__ == '__main__':
    CalcShell().cmdloop()