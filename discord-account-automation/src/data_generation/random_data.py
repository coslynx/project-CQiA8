import random
import string

def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_username():
    return ''.join(random.choices(string.ascii_letters, k=8))

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=12))

def generate_random_birthdate():
    year = random.randint(1970, 2003)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Assuming all months have 28 days for simplicity
    return f"{month}/{day}/{year}"

def generate_random_data():
    email = generate_random_email()
    username = generate_random_username()
    password = generate_random_password()
    birthdate = generate_random_birthdate()
    return email, username, password, birthdate

# Testing the random data generation
if __name__ == "__main__":
    email, username, password, birthdate = generate_random_data()
    print(f"Generated Random Data:")
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Birthdate: {birthdate}")