class Department:

    @staticmethod
    def add_department(name, budget, phone_number):
        with open("DepartmentRecords.txt", "a") as file:
            file.write(f"Name: {name}, Budget: {budget}, Phone Number: {phone_number}\n")
        print("")
        print("Department has been added successfully")
        print("")

    @staticmethod
    def remove_department(name):
        with open("DepartmentRecords.txt", "r") as file:
            lines = file.readlines()
        removed = False
        updated_lines = [line for line in lines if not line.startswith("Name: " + name)]
        if len(updated_lines) < len(lines):
            removed = True
        if not removed:
            print("")
            print("Department with name: " + name + "does not exist")
            print("")
        if removed:
            with open("DepartmentRecords.txt", "w") as file:
                file.writelines(updated_lines)
            print("")
            print("Department has been removed successfully")
            print("")

    @staticmethod
    def update_department(name, budget, phone_number):
        with open("DepartmentRecords.txt", "r") as file:
            lines = file.readlines()
        found = False
        for i, line in enumerate(lines):
            if line.startswith("Name: " + name):
                lines[i] = (
                    f"Name: {name}, "
                    f"Budget: {budget}, "
                    f"Phone Number: {phone_number}\n"
                )
                found = True
                break
        if not found:
            print("")
            print("Department with name: " + name + " does not exist")
            print("")
        else:
            with open("DepartmentRecords.txt", "w") as file:
                file.writelines(lines)
            print("")
            print("Department has been updated successfully")
            print("")

    @staticmethod
    def get_all_departments():
        with open("DepartmentRecords.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No departments exist")
            else:
                for line in lines:
                    print(line.strip())
        print("")

