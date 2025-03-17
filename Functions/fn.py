# Function definition
# def avg():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))
#     average = (a + b + c) / 3
#     print("The average of the three numbers is: ", average)

# #  Function call
# avg()


# def greet(name):
#     print("Hello, Good Morning"+ " " +name)
#     return "ok"


# a= greet("Dev")
# print(a)


def greet(name , msg = "Good morning"):
    print(f"hello , {name}")
    print(msg)

greet("Divyanshu" , "Good Night") 
greet("Dev") # Default argument   