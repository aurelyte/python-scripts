# Store the employee's first name
first_name = "John"

# Store the employee's last name
last_name = "Doe"

# Combine first name and last name into a full name
full_name = first_name + " " + last_name

# Store the employee's base address
address = "123 Main Street"

# Add apartment information to the existing address
address += ", Apartment 4B"

# Store the employee's age as an integer
employee_age = 28

# Create a sentence containing the employee's name and age
employee_info = full_name + " is " + str(employee_age) + " years old"

# Store the employee's years of experience
experience_years = 5

# Create a sentence containing the employee's experience information
experience_info = "Experience: " + str(experience_years) + " years"

# Store the employee's job position
position = "Data Analyst"

# Store the employee's salary
salary = 75000

# Create a formatted employee card using an f-string
employee_card = f"Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}"

# Store the employee code
employee_code = "DEV-2026-JD-001"

# Get the department code from the employee code
department = employee_code[0:3]

# Get the year code from the employee code
year_code = employee_code[4:8]

# Get the employee initials from the employee code
initials = employee_code[9:11]

# Print the employee's basic information
print(employee_info)

# Print the employee's experience information
print(experience_info)

# Print the formatted employee card
print(employee_card)

# Print the department code
print(department)

# Print the year code
print(year_code)

# Print the employee initials
print(initials)
