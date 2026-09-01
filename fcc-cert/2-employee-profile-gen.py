first_name = "John"

last_name = "Doe"

full_name = first_name + " " + last_name

address = "123 Main Street"

address += ", Apartment 4B"

employee_age = 28

employee_info = full_name + " is " + str(employee_age) + " years old"

experience_years = 5

experience_info = "Experience: " + str(experience_years) + " years"

position = "Data Analyst"

salary = 75000

employee_card = f"Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}"

employee_code = "DEV-2026-JD-001"

department = employee_code[0:3]

year_code = employee_code[4:8]

initials = employee_code[9:11]

print(employee_info)

print(experience_info)

print(employee_card)

print(department)

print(year_code)

print(initials)
