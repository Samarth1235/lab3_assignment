class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        return [emp for emp in self.employees if emp.age == target_age]

    def search_by_name(self, target_name):
        return [emp for emp in self.employees if emp.name == target_name]

    def search_by_salary(self, operation, target_salary):
        if operation == '>':
            return [emp for emp in self.employees if emp.salary > target_salary]
        elif operation == '<':
            return [emp for emp in self.employees if emp.salary < target_salary]
        elif operation == '<=':
            return [emp for emp in self.employees if emp.salary <= target_salary]
        elif operation == '>=':
            return [emp for emp in self.employees if emp.salary >= target_salary]
        else:
            return []

if __name__ == "__main__":
    manager = EmployeeManager()

    manager.add_employee(Employee("161E90", "Raman", 41, 56000))
    manager.add_employee(Employee("161F91", "Himadri", 38, 67500))
    manager.add_employee(Employee("161F99", "Jaya", 51, 82100))
    manager.add_employee(Employee("171E20", "Tejas", 30, 55000))
    manager.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    choice = input("Enter your choice: ")

    if choice == "1":
        target_age = int(input("Enter the age to search: "))
        result = manager.search_by_age(target_age)
    elif choice == "2":
        target_name = input("Enter the name to search: ")
        result = manager.search_by_name(target_name)
    elif choice == "3":
        operation = input("Enter the comparison operator (>, <, <=, >=): ")
        target_salary = int(input("Enter the salary to compare: "))
        result = manager.search_by_salary(operation, target_salary)
    else:
        print("Invalid choice")

    if result:
        print("Search Results:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No results found.")
