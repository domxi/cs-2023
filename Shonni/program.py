def main():
    #the vatiable
    num1 = input("First Number")
    operator = input("Operators")
    num2 = input("Second Number: ")

    #addition
    if operator == "+":
        answer = int(num1) + int(num2)

    #subtract
    if operator == "-":
        answer = int(num1) - int(num2)

    #divide
    if operator == "/":
        answer = int(num1) / int(num2)

    #multpiply
    if operator == "*":
        answer = int(num1) * int(num2)
    



    
    #this is the thing that prints out the input and output
    print(num1 + operator + num2)
    print(answer)

main()