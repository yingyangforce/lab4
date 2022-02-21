#+-----------------------+
#| lab4_3 - Isaiah Grace |
#+-----------------------+

# Tast 3 - parsing code

#---Part A---
#
# Should print out "TOP: 5 \n BOTTOM: 6"  

"""
bot = 1
mid = 5
top = 10
while bot < mid and top > mid:
    bot += 1
    top -= 1
print("TOP:    ", top)
print("BOTTOM: ", bot)
"""


#---Part B---
#
#   Should return 4 as an integer.

"""
def FunctionA(numA):
    return numA // 2

def FunctionB(numB):
    if numB % 2 == 1:
        return FunctionA(numB - 1)
    else:
        return numB

def FunctionC(numC):
    if numC > 10:
        return FunctionB(numC // 3)
    else:
        return FunctionA(numC + 10)

def main():
    num = 27
    print(FunctionC(num))
main()
"""


#---Part C---
#
#   Should print "Total: 10".

"""
w = 100
h = 20
total = 0

x = 0
while x < 2:
    y = 0
    while y < h:
        total += 1
        y += 4
    x += 2

print("Total: ", total)
"""


