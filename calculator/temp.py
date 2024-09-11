                 #CALCULATOR#

number1 = int(input("enter a number  : "))
print("first number : " ,  number1 )

number2 = int(input("enter a number: "))
print("second number : " , number2)

operation =input("select the operation you want to do : ")

if operation  == "+":
    print("sum of first and second number : ",number1 + number2)

elif operation == "-":
    print("difference of first and second number : ",number1 - number2)

elif  operation == "/":
    if number2==0 : 
        print("division error...")
    else :
        print("division of first and second numbers: ",number1 / number2)

elif operation == "*":
    print("multiplication of first and second number : ",number1 * number2)

else :
    print("you choose the wrong operation...")


