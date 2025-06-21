import csv
from faker import Faker
import random
import string


# Specify number of employees to generate
num_employees = 50

# Create Faker instance
fake = Faker()

# Define the character set for the password
password_characters = string.ascii_letters + string.digits + 'm'

# Generate employee data and save it to a CSV file
with open('employee_data.csv', mode='w', newline='') as file:
    fieldnames = ['first_name', 'last_name', 'job_title', 'department', 'email', 'address', 'phone_number', 'salary', 'password']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(num_employees):
        writer.writerow({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job_title": fake.job(),
            "department": fake.job(),  # Generate department-like data using the job() method
            "email": fake.email(),
            "address": fake.city(),
            "phone_number": fake.phone_number(),
            "salary": fake.random_number(digits=5),  # Generate a random 5-digit salary
            "password": ''.join(random.choice(password_characters) for _ in range(8))  # Generate an 8-character password with 'm'
        })