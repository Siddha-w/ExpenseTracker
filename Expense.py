import os

filename = "expenses.txt"

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Expense Name: ")
        category = input("Enter Category: ")
        amount = int(input("Enter Amount: "))

        file = open(filename, "a")
        file.write(f"{name},{category},{amount}\n")
        file.close()

        print("Expense Added Successfully!")

    elif choice == "2":
        if os.path.exists(filename):
            file = open(filename, "r")
            print("\nExpense Name\tCategory\tAmount")
            print("-" * 40)
            for line in file:
                data = line.strip().split(",")
                print(data[0], "\t\t", data[1], "\t\t", data[2])
            file.close()
        else:
            print("No expenses found!")

    elif choice == "3":
        total = 0

        if os.path.exists(filename):
            file = open(filename, "r")
            for line in file:
                data = line.strip().split(",")
                total += float(data[2])
            file.close()

        print("Total Expense: ₹", total)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")