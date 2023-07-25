def main():
    num1 = input("fristnumber: ")
    operator = input("Operartor: ")
    num2 = input("Secound Number: ")
    answer = None

    #addition
    if operator == "+":
        answer = int(num1) + int(num2)

    #addition
    if operator == "-":
        answer = int(num1) - int(num2)

    #addition
    if operator == "*":
        answer = int(num1) * int(num2)

    #addition
    if operator == "/":
        answer = int(num1) / int(num2)



    print(num1 + operator + num2)
    print(answer)

main()