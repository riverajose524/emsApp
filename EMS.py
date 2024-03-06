from Employee import Employee


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
        print("* 5: Exit                                *")
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
            print("Until next time. Goodbye!")
        else:
            print("You made an incorrect choice")
            self.EMS_menu()
        
    def add_employee(self):
        first_name = input("Enter employee's first name: ")
        last_name = input("Enter employee's last name: ")
        date_of_employmemt = input("Enter employee's date of employment: ")
        salary = input("Enter employee's annual salary: ")
        department = input("Enter the department name the employee works in: ")

        print("")
        print("Employee has been added successfully")
        print("")

    def update_employee(self):
        first_name = input("Enter employee's first name: ")
        last_name = input("Enter employee's last name: ")
        date_of_employmemt = input("Enter employee's date of employment: ")
        salary = input("Enter employee's annual salary: ")
        department = input("Enter the department name the employee works in: ")
        
        print("")
        print("Employee has been updated successfully")
        print("")

    def remove_employee(self):
        id_number = input("Enter employee's id #: ")
        
        print("")
        print("Employee has been removed successfully")
        print("")

    def get_employees_info(self):
        print("Employee's information ")
        print("")

    
