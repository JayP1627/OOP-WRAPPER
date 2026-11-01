class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary:.2f}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        print("\nManager Details:")
        super().show_details()
        print(f"Department: {self.department}")


def main():
    records = {}

    while True:
        print("""
        ===== Employee Management System =====
        1. Create a Person
        2. Create an Employee
        3. Create a Manager
        4. Show Details
        5. Exit
        """)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            records["1"] = Person(name, age)
            print(f"Person created with name:{name} and age: {age}")

        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            records["2"] = Employee(name, age, emp_id, salary)
            print(f"Employee created with name: {name}, age {age},ID:{emp_id},and salary:{salary}")

        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")

            records["3"] = Manager(
                name, age, emp_id, salary, department
            )
            print(f" Manager created with name:{name},age:{age},ID:{emp_id},salary:{salary}")

        elif choice == "4":
            sub_choice = input(
                "Show details (1.Person, 2.Employee, 3.Manager): "
            ).strip()

            if sub_choice in records:
                records[sub_choice].show_details()
            else:
                print("No details found. Create a record first.")

        elif choice == "5":
            print("Exiting the system.All resources have been freed.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()