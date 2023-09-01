def min_num(num1:float, num2:float, num3:float)->float:
    if num1 <= num2 and num1 <= num3:
        return num1
    if num3<= num1 and num3 <= num2 :
        return num3
    else: 
        return num2

print (min_num(5,4.5,1))