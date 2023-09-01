"erster Taschenrechner"

#num1= input("What's your first number? :")
#num2= input("What's your second number? :")
#result= float(num1) + float(num2)
#print(result)



num1 = float(input("Was ist die erste Zahl: "))
op = (input("Was ist der Operator: "))
num2 = float(input("Was ist die zweite Zahl: "))

if op== "+":
    print(num1+num2)
elif op== "-":
    print(num1-num2)
elif op== "/":
    print(num1/num2)
elif op== "*":
    print(num1*num2)   
else:
    print("Operator ist nicht im Programm")