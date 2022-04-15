# 3 STEPS FOR WRITING RECURSION ALGORITHM 
# i. BUILD A RECURSIVE CASE - THIS DESCRIBES THE FLOW (GOVERNING EQN AND LOGIC)
# ii. SPECIFY A BASE CASE - THIS IS A STOPPING CRITERION TO PREVENT AN INFINITE LOOP
# iii. IDENTIFY THE UNINTENTIONAL CASE - THIS PLACES A CONSTRAINT TO THE ALGORITHM

            # USING RECURSION FOR POWER OF TWO
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power*2
print(powerOfTwo(4))

            # USING RECURSION FOR FACTORIAL
def factorial(n):
    assert n>=0 and int(n) == n, "The number must be a positive integer only"
    if n in [0,1]: 
        return 1
    else:
        return n*factorial(n-1)
print(factorial(12))

            # USING RECURSION FOR FIBONACCI
def fibonacci(n):
    assert n>=0 and int(n) == n, "The number must be a positive integer only"
    if n in [0,1]: 
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(2))

            # USING RECURSION TO FIND THE SUM OF DIGITS OF A POSITIVE INTEGER
def sumOfDigits(n):
    assert n>=0 and int(n) == n, "The number must be a positive integer only"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))
print(sumOfDigits(123))

            # USING RECURSION TO CALCULATE THE POWER OF A NUMBER
def power(base,exp):
    assert exp>=0 and int(exp)==exp, "we're dealing with positive numbers only"
    if exp==0:
        return 1
    if exp==1:
        return base
    else:
        return base*power(base,exp-1)
print(power(2,4))

            # GREATEST COMMON DIVISOR OF 2 NUMBER USING RECURSSION AND EUCLIDEAN ALGORITHM
def gcd(a,b):
    assert int(a)== a and int(b) == b, "The number must be integer only"
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1*b
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,-18))

            # CONVERTING DECIMAL TO BINARY USING RECURSION
def decimalToBinary(n):
    assert int(n) == n, "The parameter must be an integer only"
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(int(n/2))
print(decimalToBinary(13))

            #RECURSIVE ALGOROITHM THAT DRAWS A RULER
def draw_line(tick_length, tick_label = ''):
    #Draws one line with given tick length
    line = ' ' + tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    #Draws tick interval based upon a central tick length
    if center_length > 0:                #stop when lemgth drops to 0
        draw_interval(center_length - 1) #recursively draw top ticks
        draw_interval(center_length)     #draw center tick
        draw_interval(center_length - 1) #recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    #Draws English ruler with given number of inches , major tick length
    draw_line(major_length, '0')         #draws inch 0 line
    for j in range (1, 1 + num_inches):
        draw_interval(major_length - 1)  #draw interior ticks for inch
        draw_line(major_length, str(j))  #draw inch j line and label
draw_interval(3)

            #AREA PROBLEM ON LEETCODE
        #MY SOLUTION
def areaprob(area):
    answer = []
    multiples = []
    for i in range(1,int(area)+1):
        for j in range(1,int(area)+1):
            if i*j == area:
                if i >= j:
                    multiples.append([i,j])
    return multiples[0]
print(areaprob(4))

        #REVISED SOLUTION
def areaprob(area):
    multiples = []
    for i in range(1,int(area)+1):
        j = area // i
        if i*j == area:
            if i <= j:
                multiples.append([max(i,j),min(i,j)])
    return multiples[-1]
print(areaprob(47))

