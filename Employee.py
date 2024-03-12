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
        id_number = Employee.get_last_id() + 1
        print(id_number)
        with open("employeeRecords.txt", "a") as file:
            file.write(f"Id: {id_number} (First Name: {first_name}, Last Name: {last_name}, Date of Employment: {date_of_employment}, Salary: {salary}, Department: {department})\n")

        print("")
        print("Employee has been added successfully")
        print("")
    
    def update_employee(id_number, first_name, last_name, date_of_employment,
                    salary, department):
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
                        f"Department: {department}}}\n"
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
                        department = department.rstrip("}")
                        department = department.rstrip(")")

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
            

        
        
        
        
        
        

        
        
