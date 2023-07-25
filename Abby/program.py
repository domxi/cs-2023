def main():
    num1 = input("first #: ")
    operator = input("operator: ")
    num2 = input("second #: ")
    answer = None

    #addition
    if operator == "+":
        answer = int(num1) + int(num2)
    #subtraction
    if operator == "-":
        answer = int(num1) - int(num2)
    #multiplication
    if operator == "*":
        answer = int(num1) * int(num2)
    #division
    if operator == "/":
        answer = int(num1) / int(num2)
    
    print(num1 + operator + num2)
    print(answer)


main()
