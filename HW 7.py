Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1. a) definite loops run a called number of times, indefinite loops run until some condition is met
# b) a for loop is a type of definite loop so the number of times it runs is defined. a while loop is a type of indefinite loop so the number of runs is not defined
# c) interactive loops interact with the user to determine when to stop, sentinel loops have a predetermined stopping point
# d) sentinel loops stop when some value is reached, end of file loops stop once the end of the file has been detected
# p  q  r  not(p and q)  not(p) and q  (not p) or (not q)  (p and q) or r  (p or r) and (q or r)
# T  T  T      F              F                F                   T                T
# T  T  F      F              F                F                   T                T
# T  F  T      F              F                T                   T                T
# F  T  T      F              T                T                   T                T

# T  F  F      F              F                T                   F                F
# F  T  F      F              T                T                   F                F
# F  F  T      T              F                T                   T                T
# F  F  F      T              F                T                   F                F

def main():
    sum = 0
    n = input("enter a number: ")
    while n > 0:
        x = n
        sum = x + sum
        n = n - 1

        
def main():
    sum = 0
    n = input("enter a number: ")
    while n > 0:
        x = n
        sum = x + sum
        n = n - 1
    print("The sum is",sum)

    
main()
enter a number: 7
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    main()
  File "<pyshell#25>", line 4, in main
    while n > 0:
TypeError: '>' not supported between instances of 'str' and 'int'
def main():
    sum = 0
    n = eval(input("enter a number: "))
    while n > 0:
        x = n
        sum = x + sum
        n = n - 1
    print("The sum is",sum)

main()
enter a number: 7
The sum is 28

def main():
    n = eval(input("What number in the Fibonnaci sequence would you like to see?: "))
    count = 0
    x = 1
    y = 0

    while count < n:
        count = count + 1
        z = x + y
        x = y
        y = z
    print(z)

    
main()
What number in the Fibonnaci sequence would you like to see?: 6
8

def syr(x):
    if x % 2 == 0:
        syrX = x/2
    elif x % 2 == 1:
        syrX = 3 * x + 1
    return syrX

def main():
    x = eval(input("Input a natural number: "))
    print(x)
    while x > 1:
        syrX = syr(x)
        x = syrX
        print(syrX)
        
SyntaxError: invalid syntax
def syr(x):
    if x % 2 == 0:
        syrX = x/2
    elif x % 2 == 1:
        syrX = 3 * x + 1
    return syrX
def main():
    x = eval(input("Input a natural number: "))
    print(x)
    while x > 1:
        syrX = syr(x)
        x = syrX
        print(syrX)
        
SyntaxError: invalid syntax

def syr(x):
    if x % 2 == 0:
        syrX = x/2
    elif x % 2 == 1:
        syrX = 3 * x + 1
    return syrX
def main():
    x = eval(input("Input a natural number: "))
    print(x)
    while x > 1:
        syrX = syr(x)
        x = syrX
        print(syrX)
        
SyntaxError: invalid syntax
def syr(x):
    if x % 2 == 0:
        syrX = x/2
    elif x % 2 == 1:
        syrX = 3 * x + 1
    return syrX

def main():
    x = eval(input("Input a natural number: "))
    print(x)
    while x > 1:
        syrX = syr(x)
        x = syrX
        print(syrX)

        
main()
Input a natural number: 7
7
22
11.0
34.0
17.0
52.0
26.0
13.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0
