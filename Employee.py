from EmployeeNotFoundException import EmployeeNotFoundException

class Employee:

    @classmethod
    def get_last_id(cls):
        with open("employeeRecords.txt", "r") as file:
            lines = file.readlines()

            if lines:
                last_line = lines[-1]
                last_id = last_line.split(':')[1].strip()
                last_id = ''.join(filter(str.isdigit, last_id))
                return int(last_id) if last_id else 0
            else:
                return 0

    @staticmethod
    def add_employee(first_name, last_name, date_of_employment, salary, department):
        department_exists, department_info = Employee.get_department_info(department)

        if department_exists:
            id_number = Employee.get_last_id() + 1
            with open("employeeRecords.txt", "a") as file:
                file.write(f"Id: {id_number} (First Name: {first_name}, Last Name: {last_name}, Date of Employment: {date_of_employment}, Salary: {salary}, Department: ({department_info}))\n")
                print("")
                print("Employee has been added successfully")
                print("")
        else:
            print("")
            print("Error: Department does not exist. Employee not added.")
            print("")

    @staticmethod
    def update_employee(id_number, first_name, last_name, date_of_employment, salary, department):
        department_exists, department_info = Employee.get_department_info(department)

        if department_exists:
            try:
                with open("employeeRecords.txt", "r") as file:
                    lines = file.readlines()
                found = False
                for i, line in enumerate(lines):
                    if line.startswith("Id: " + str(id_number)):
                        lines[i] = (
                            f"Id: {id_number} "
                            f"{{First Name: {first_name}, "
                            f"Last Name: {last_name}, "
                            f"Date of Employment: {date_of_employment}, "
                            f"Salary: {salary}, "
                            f"Department: ({department_info})}}\n"
                        )
                        found = True
                        break
                if not found:
                    raise EmployeeNotFoundException
                else:
                    with open("employeeRecords.txt", "w") as file:
                        file.writelines(lines)
                    print("")
                    print("Employee has been updated successfully")
                    print("")
            except EmployeeNotFoundException:
                print("")
                print("Exception occurred: Employee with ID " + id_number + " not found")
                print("")
        else:
            print("")
            print("Error: Department does not exist. Employee not updated.")
            print("")

    @staticmethod
    def get_department_info(department):
        try:
            with open("DepartmentRecords.txt", "r") as file:
                for line in file:
                    if department in line:
                        return True, line.strip()
            return False, None
        except FileNotFoundError:
            print("Department records file not found.")
            return False, None

    @staticmethod
    def remove_employee(id_number):
        try:
            with open("employeeRecords.txt", "r") as file:
               lines = file.readlines()
            removed = False
            updated_lines = [line for line in lines if not line.startswith("Id: " + str(id_number))]
            if len(updated_lines) < len(lines):
                removed = True
            if not removed:
                raise EmployeeNotFoundException
            if removed:
                with open("employeeRecords.txt", "w") as file:
                    file.writelines(updated_lines)
            print("")
            print("Employee has been removed successfully")
            print("")
        except EmployeeNotFoundException:
            print("")
            print("Exception occurred: Employee with ID " + id_number + " not found")
            print("")
        
    @staticmethod
    def get_employee_info(id_number):
        found = False

        try:
            with open("employeeRecords.txt", "r") as file:
                for line in file:
                    if line.startswith("Id: " + id_number):
                        found = True
                        data = line.split()
                        emp_id = data[1]
                        first_name = data[4]
                        last_name = data[7]
                        date_of_employment = data[11]
                        salary = data[13]
                        department = " ".join(data[15:])
                        department = department.strip(")").split("(")[1]

                        print("")
                        print(f"ID: {emp_id}")
                        print(f"First Name: {first_name}")
                        print(f"Last Name: {last_name}")
                        print(f"Date of Employment: {date_of_employment}")
                        print(f"Salary: {salary}")
                        print(f"Department: {department}")
                        print("")
                        break

            if not found:
                raise EmployeeNotFoundException

        except EmployeeNotFoundException:
            print("")
            print("Exception occurred: Employee with ID " + id_number + " not found")
            print("")

    @staticmethod
    def get_employees_by_department(name):
        found = False

        try:
            with open("employeeRecords.txt", "r") as file:
                for line in file:
                    if f"Department: (Name: {name}" in line:
                        found = True
                        data = line.split()
                        emp_id = data[1]
                        first_name = data[4]
                        last_name = data[7]
                        date_of_employment = data[11]
                        salary = data[13]
                        department_info = " ".join(data[15:])
                        department_info = department_info.strip(")").split("(")[1]
                        print("")
                        print(f"ID: {emp_id}")
                        print(f"First Name: {first_name}")
                        print(f"Last Name: {last_name}")
                        print(f"Date of Employment: {date_of_employment}")
                        print(f"Salary: {salary}")
                        print(f"Department: {department_info}")
                        print("")
            if not found:
                    raise EmployeeNotFoundException
        except EmployeeNotFoundException:
            print("")
            print("Exception occurred: No employees found in the department: " + name)
            print("")
        
            

        
        
        
        
        
        

        
        
