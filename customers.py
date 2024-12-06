import pandas as pd
import random
from faker import Faker
from datetime import datetime

# Initialize Faker with an Indian locale
fake = Faker('en_IN')

# Define the number of records
num_records = 8000

# List of Indian cities
indian_cities = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune",
    "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam",
    "Pimpri-Chinchwad", "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik"
]

# Convert start and end dates to datetime.date objects
start_date = datetime.strptime("2020-01-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-12-31", "%Y-%m-%d").date()


# Generate unique customer IDs
customer_ids = [f"CUST{str(i).zfill(5)}" for i in range(1, num_records + 1)]

# Generate random Indian names
names = [fake.name() for _ in range(num_records)]

# Generate random Indian cities
cities = random.choices(indian_cities, k=num_records)

# Generate random signup dates
signup_dates = [fake.date_between(start_date=start_date, end_date=end_date) for _ in range(num_records)]

# Generate random referral sources
referral_sources = random.choices(
    ["Instagram", "Facebook", "Google Ads", "Friend Referral", "TV Ad", "Newspaper Ad","Email Campaign", "Direct Visit"],
    k=num_records
)

# Generate random genders
genders = random.choices(["Male", "Female"], k=num_records)

# Generate random ages
ages = [random.randint(18, 65) for _ in range(num_records)]

# Create the DataFrame
customers_df = pd.DataFrame({
    "customer_id": customer_ids,
    "name": names,
    "gender": genders,
    "age": ages,
    "city": cities,
    "signup_date": signup_dates,
    "referral_source": referral_sources
    
})

# Save the DataFrame to a CSV file
customers_df.to_csv("customers.csv", index=False)

# Print a sample of the generated data
print(customers_df.head())
