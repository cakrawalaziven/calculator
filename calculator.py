print(20*"_","\n",3*" ","CALCULATOR")

name = input("What is your name : ")
print("Hello",name)
Num1 = float(input("\nEnter number : "))
Op = input("Enter operator (+ , - , * , /) : ")
Num2 = float(input("Enter another number : "))

if Op == "+":
    print("The calculation of",Num1,"and",Num2,"is:",Num1 + Num2)
elif Op == "-":
    print("The calculation of",Num1,"and",Num2,"is:",Num1 - Num2)
elif Op == "*":
    print("The calculation of",Num1,"and",Num2,"is:",Num1 * Num2)
elif Op == "/":
    print("The calculation of",Num1,"and",Num2,"is:",Num1 / Num2)
else:
    print("Please enter * or / or + or -.")