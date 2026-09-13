###    MINI CALCULATOR ###

menu = """
 1. Add (+)
 2. Subtract (-)
 3. Multiply (*)
 4. Divide (/)
 5. Quit
 """
print(menu)
choice = input("Choose 1-5: ")

if choice == "5":
    print("Goodbye!")

if choice in ["1", "2", "3", "4"]:
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))
    result = ""
    if choice == "1":
        result = (num1 + num2)
    elif choice == "2":
        result = (num1 - num2)
    elif choice == "3":
        result = (num1 * num2)
    else:
        if num2 == 0:
            result = ("Cannot divide by zero!")
        else:
            result = (num1 / num2)
print("Results:", result)
