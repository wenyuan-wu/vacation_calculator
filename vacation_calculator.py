import datetime
import calendar

# Define the total number of vacation days
total_vacation_days = 25

# Prompt the user to enter their employment date
employment_date_str = input("Enter your employment date (YYYY-MM-DD): ")

# Convert the employment date string to a datetime object
try:
    employment_date = datetime.datetime.strptime(employment_date_str, '%Y-%m-%d')
except ValueError as e:
    print("Error: Invalid employment date format. Please enter the date in the format YYYY-MM-DD.")
    exit()

# Calculate the number of days worked
current_year = datetime.date.today().year
last_day_of_year = datetime.datetime(current_year, 12, 31)
total_days_in_year = calendar.isleap(current_year) + 365
days_worked = (last_day_of_year - employment_date).days + 1

# Calculate the prorated vacation days
prorated_vacation_days = (days_worked / total_days_in_year) * total_vacation_days

# Print the result with verbose explanation
print("Total vacation days:", total_vacation_days)
print("Employment date:", employment_date)
print("Days (should have) worked:", days_worked)
print("Prorated vacation days:", prorated_vacation_days)
