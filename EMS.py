from Employee import Employee
from Department import Department


class EMS:

    def __init__(self):
        pass

    def EMS_menu(self):
        print("******************************************")
        print("*       Employee Management System       *")
        print("******************************************")
        print("*       What would you like to do?       *")
        print("*                                        *")
        print("* 1: Add employee                        *")
        print("* 2: Update employee                     *")
        print("* 3: Remove employee                     *")
        print("* 4: Get an employee's information       *")
        print("* 5: Get all employees by department     *")
        print("* 6: Add department                      *")
        print("* 7: Update department                   *")
        print("* 8: Remove department                   *")
        print("* 9: Get all departments                 *")
        print("* 10: Exit                               *")
        print("******************************************")

        choice = input();
        print("")

        if choice == "1":
            self.add_employee()
            self.EMS_menu()
        elif choice == "2":
            self.update_employee()
            self.EMS_menu()
        elif choice == "3":
            self.remove_employee()
            self.EMS_menu()
        elif choice == "4":
            self.get_employees_info()
            self.EMS_menu()
        elif choice == "5":
            self.get_employee_by_department()
            self.EMS_menu()
        elif choice == "6":
            self.add_department()
            self.EMS_menu()
        elif choice == "7":
            self.update_department()
            self.EMS_menu()
        elif choice == "8":
            self.remove_department()
            self.EMS_menu()
        elif choice == "9":
            self.get_all_departments()
            self.EMS_menu()
        elif choice == "10":
            print("Until next time. Goodbye!")
        else:
            print("You made an incorrect choice")
            print("")
            self.EMS_menu()
        
    def add_employee(self):
        first_name = input("Enter employee's first name: ")
        last_name = input("Enter employee's last name: ")
        date_of_employment = input("Enter employee's date of employment: ")
        salary = input("Enter employee's annual salary: ")
        department = input("Enter the department name the employee works in: ")

        Employee.add_employee(first_name, last_name, date_of_employment,
                              salary, department)      

    def update_employee(self):
        id_number = input("Enter the employee's id number: ")
        first_name = input("Enter employee's first name: ")
        last_name = input("Enter employee's last name: ")
        date_of_employment = input("Enter employee's date of employment: ")
        salary = input("Enter employee's annual salary: ")
        department = input("Enter the department name: ")
        
        Employee.update_employee(id_number, first_name, last_name,
                                 date_of_employment, salary, department)

    def get_employee_by_department(self):
        name = input("Enter the department name: ")
        Employee.get_employees_by_department(name)
        

    def remove_employee(self):
        id_number = input("Enter employee's id #: ")

        Employee.remove_employee(id_number)


    def get_employees_info(self):
        id_number = input("Enter employee's id #: ")

        Employee.get_employee_info(id_number)

    def add_department(self):
        name = input("Enter department name: ")
        budget = input("Enter department's budget: ")
        phone_number = input("Enter department's phone number: ")
        Department.add_department(name, budget, phone_number)

    def update_department(self):
        name = input("Enter department name: ")
        budget = input("Enter department's budget: ")
        phone_number = input("Enter department's phone number: ")
        Department.update_department(name, budget, phone_number)
        
    def remove_department(self):
        name = input("Enter department name: ")
        Department.remove_department(name)

    def get_all_departments(self):
        Department.get_all_departments()

    
