#+-----------------------+
#| lab4_2 - Isaiah Grace |
#+-----------------------+

# Task 2 - Whimsical while loops

import os

#---Part A---
def partA():
    odd_num = 1

    while odd_num < 100:
        print(odd_num)
        odd_num += 2

    while odd_num > 0:
        odd_num -= 2
        print(odd_num)

#partA()
#---Part B---
def Sum(value):
    acc = 1
    counter = 1

    while counter != value:
        counter += 1
        acc += counter

    return acc
        
#print(Sum(5))

#---Part C---
def partC():
    numA = int(input("Input first number: "))
    numB = int(input("Input second number: "))

    while numA > 0:
        print("Outer")
        numA -= 1
        b_count = numB
        while b_count > 0:
            print("Inner")
            b_count -= 1
#partC()

#---Part D---
def sentinelLoop():
    isOuterOn = True

    while isOuterOn:
        isInnerOn = True

        os.system("clear")
        print("Outer layer")

        outer_input = input("Enter [q] to exit outer loop: ")
        if outer_input == "q":
            return

        while isInnerOn:
            print("\nInner layer")

            inner_input = input("Enter [quit] to exit inner loop, enter [q] to exit outer loop: ")

            if inner_input == "q":
                return
            if inner_input == "quit":
                break

#sentinelLoop()

