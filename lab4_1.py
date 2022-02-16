#+-----------------------+
#| lab4_1 - Isaiah Grace |
#+-----------------------+

# Task 1- Fun with functions

def AbsVal(num): # Part A
    return num if num > 0 else num * -1 if num < 0 else 0

def IntRound(num): # Part B
    return int(num) if num % 1 < 0.5 else int(num) + 1

def ConvertTemp(temp, scale): # Part C
    toC = lambda temp : (temp - 32) / 1.8
    toF = lambda temp : (temp * 1.8) + 32
    return toF(temp) if scale == 'C' else toC(temp)

