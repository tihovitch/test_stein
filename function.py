def sayhi(name:str, age:int)->None:
    """
    To do
    """
    print("Hello "+ name +", you are "+ str(age))

sayhi("Lara", 3)
sayhi("kam", 65)


def cube(num:int, skal: int = 1)->int:
    return num*num*num+skal

result=cube(4)
print(result)

result=cube(4, 2)
print(result)


