def main():
    num1=input("First #: ")
    operator=input("Operator: ")
    num2=input("second #: ")
    answer=None


    #add
    if operator == "+": 
        answer = int(num1) + int(num2)  
    #subtract
    if operator == "-": 
        answer = int(num1) - int(num2) 
    #divide
    if operator == "/": 
        answer = int(num1) / int(num2)
    #multiply
    if operator == "*": 
        answer = int(num1) * int(num2)
    print(num1+ operator + num2)
    print(answer)


main()