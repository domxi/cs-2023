# def hello():
#     print("Hello")


def main():
    num1 = input("First Number: ")
    operator = input("Operator: ")
    num2 = input("Second Number: ")
    answer = None

    # addition
    if operator == "+":
        answer = int(num1) + int(num2)
    
    # subtraction
    if operator == "-":
        answer = int(num1) - int(num2)

    # multiplication
    if operator == "*":
        answer = int(num1) * int(num2)

    # division
    if operator == "/":
        answer = int(num1) / int(num2)
    
    # mod - Remainder
    if operator == "%":
        answer = int(num1) % int(num2)

    print(num1 + operator + num2)
    print(answer)

# Call function ---------------------------------
#hello()
main()