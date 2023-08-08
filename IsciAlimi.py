from dataclasses import dataclass

class Employee:
    def __init__(self, empcode, name, addr, phno, date, desg, grade, loan, bs, hs):
        self.empcode = empcode
        self.name = name
        self.addr = addr
        self.phno = phno
        self.date = date
        self.desg = desg
        self.grade = grade
        self.loan = loan
        self.bs = bs
        self.hs = hs

    def input(self):
        self.empcode = int(input("Enter empcode: "))
        input()
        self.name = input("Enter Name: ")
        self.addr = input("Enter Address: ")
        self.phno = input("Enter Phone Number: ")
        self.date = input("Enter Date (dd/mm/yy): ")
        self.desg = input("Enter Designation: ")
        self.grade = input("Enter Grade: ")
        self.loan = float(input("Enter Loan: "))
        self.bs = float(input("Enter Basic Salary: "))
        self.hs = float(input("Enter House Allowance: "))

    def display(self):
        print("Empcode:", self.empcode)
        print("Name:", self.name)
        print("Address:", self.addr)
        print("Phone Number:", self.phno)
        print("Date(dd/mm/yy):", self.date)
        print("Designation:", self.desg)
        print("Grade:", self.grade)
        print("Loan:", self.loan)
        print("Basic Salary:", self.bs)
        print("House Allowance:", self.hs)

    def write_to_file(self):
        with open("python.csv", "a") as file:
            file.write("Empcode: " + str(self.empcode) + "\n")
            file.write("Name: " + self.name + "\n")
            file.write("Address: " + self.addr + "\n")
            file.write("Phone Number: " + self.phno + "\n")
            file.write("Date(dd/mm/yy): " + self.date + "\n")
            file.write("Designation: " + self.desg + "\n")
            file.write("Grade: " + self.grade + "\n")
            file.write("Loan: " + str(self.loan) + "\n")
            file.write("Basic Salary: " + str(self.bs) + "\n")
            file.write("House Allowance: " + str(self.hs) + "\n")

    def print_slip(self):
        days = int(input("Enter number of Days Employee Worked: "))
        hours = int(input("Enter number of Hours Employee Worked: "))
        gross = (self.bs + self.hs) / 176  # rate per hour, assuming 20 days per month and 8 hours a day
        gross = gross * (days * hours)  # net gross per month
        tax = gross * 0.15  # tax at 15% of salary
        print("GROSS SALARY:", gross)
        print("TAX AT 15%:", tax)
        print("NET:", gross - tax)


class ManagementSystem:
    def __init__(self):
        self.emp = []

    def display(self):
        for employee in self.emp:
            employee.display()

    def search(self):
        emp_code = int(input("Enter an Employee Code: "))
        for employee in self.emp:
            if employee.empcode == emp_code:
                return employee
        return None

    def delete(self):
        emp_code = int(input("Enter an Employee Code: "))
        for employee in self.emp:
            if employee.empcode == emp_code:
                self.emp.remove(employee)
                return True
        return False


M = ManagementSystem()

while True:
    print("1. Add New Employee")
    print("2. Modify Employee Record")
    print("3. Delete Employee Record")
    print("4. Print Salary Slip")
    print("5. Display an Employee Record")
    print("6. Display List of Employees")
    print("7. Write to File")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        E = Employee(None, None, None, None, None, None, None, None, None, None)
        E.input()
        M.emp.append(E)
    elif choice == 2:
        E = M.search()
        if E:
            E.input()
        else:
            print("Employee not found")
    elif choice == 3:
        result = M.delete()
        if result:
            print("SUCCESSFUL DELETE")
        else:
            print("Employee not found")
    elif choice == 4:
        E = M.search()
        if E:
            E.print_slip()
        else:
            print("Employee not found")
    elif choice == 5:
        E = M.search()
        if E:
            E.display()
        else:
            print("Employee not found")
    elif choice == 6:
        M.display()
    elif choice == 7:
        for employee in M.emp:
            employee.write_to_file()
    elif choice == 8:
        print("Program terminated")
        break
    else:
        print("Enter a valid choice")
