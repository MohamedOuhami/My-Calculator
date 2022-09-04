# Creating my calculator which will add, substact, multiply, divide, find square root, find power and find the modulo

# Getting both the numbers and the desired operation
print("PLease, enter 2 numbers")
num1 = float(input("Give me your first number :"))
num2 = float(input("Give me your second number :"))
print("Type the correspondant code for each operation in the prompt given \nHere are the list of operations available for now: \n\tAddition : add \n\tSubstraction : sub \n\tMultiplication : mult \n\tDivide : div \n\tSquare root : sqrt \n\tPower : pow \n\tModulo : mod")
oper = str(input("Give me your desired operation : ")).lower()

# Addition
if(oper == "add") :
    print("Your operation was addition. The result is " + str(num1 +num2))


# Substraction
if(oper == "subs") : 
    print("Your operation was substraction. The result is " + str(num1 -num2))


# Multiplication
if(oper == "mult") :
    print("Your operation was multiplication. The result is " + str(num1 *num2))


# Division
if(oper == "div") :
    print("Your operation was division. The result is " + str(num1 /num2))


# Square Root
if(oper == "sqrt") :
    print("Your operation was square rooting. The result is " + str(sqrt(num1)))


# Power
if(oper == "pow") :
    print("Your operation was power. The result is " + str(pow(num1, num2)))


# Modulo
if(oper == "mod") :
    print("Your operation was modulo. The result is " + str(num1 %num2))

