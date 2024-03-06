class Employee:

    id_counter = 0

    def __init__(self, first_name, last_name, date_of_employment,
                 salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_employment = date_of_employment
        self.salary = salary
        self.department = department
        self.id = Employee.id_counter
        Employee.id_counter +=1

    def add_employee(self):
        file = open("employeeRecords.txt", "a")
        file.write("Id: " + self.id + " First Name: " + self.first_name
                   " Last Name: " + self.last_name + " Date of Employment: "
                   + self.date_of_employment + " Salary: " + salary
                   + " Department: " + self.department)
        file.close()

    def update_employee(self, first_name, last_name, date_of_employment,
                        salary, department):
        with open("employeeRecords.txt", "r") as file:
            lines = file.readlines()

        self.first_name = first_name
        self.last_name = last_name
        self.date_of_employment = date_of_employment
        self.salary = salary
        self.department = department

        for i, line in enumerate(lines):
            if line.startswith("Id: " + self.id):
                lines[i] = (
                    f"Id: {self.id} "
                    f"First Name: {first_name} "
                    f"Last Name: {last_name} "
                    f"Date of Employment: {date_of_employment} "
                    f"Salary: {salary} "
                    f"Department: {department}\n"
                    )
                    break
        with open("employeeRecords.txt", "w") as file:
            file.writelines(lines)


    def remove_employee(self):
        with open("employeeRecords.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith("Id: " + self.id):
                del lines[i]
                break
        with open("employeeRecords.txt", "w") as file:
            file.writelines(lines)

    def get_employee_info(self):
        found = False
    
        
        with open("employeeRecords.txt", "r") as file:
            for line in file:
                if line.startswith("Id: " + self.id): 
                    found = True
                    data = line.split()
                    emp_id = data[1]
                    first_name = data[3]
                    last_name = data[5]
                    date_of_employment = data[7]
                    salary = data[9]
                    department = data[11]
                
                    print("Employee Information:")
                    print(f"ID: {emp_id}")
                    print(f"First Name: {first_name}")
                    print(f"Last Name: {last_name}")
                    print(f"Date of Employment: {date_of_employment}")
                    print(f"Salary: {salary}")
                    print(f"Department: {department}")
                    print("")
                    break
    
        if not found:
            print("Employee not found.")
            print("")

        
        
        
        
        
        

        
        
