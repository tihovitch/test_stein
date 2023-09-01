def max_number(num1:float, num2: float , num3: float)->float:
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2>= num1 and num2>= num3:
        return num2
    else:
        return num3

print(max_number(13, 33, 46 ))

