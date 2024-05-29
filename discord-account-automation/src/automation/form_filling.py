import requests
import random
from data_generation.random_data import generate_random_email, generate_random_username, generate_random_password, generate_random_birthdate
from error_handling.error_handling import handle_error
from logging.logging import log_action

def fill_form():
    email = generate_random_email()
    username = generate_random_username()
    password = generate_random_password()
    birthdate = generate_random_birthdate()

    data = {
        'email': email,
        'username': username,
        'password': password,
        'birthdate': birthdate
    }

    try:
        response = requests.post('https://discord.com/api/register', data=data)
        response.raise_for_status()
        log_action(f'Form filled successfully for {username}')
    except requests.exceptions.RequestException as e:
        handle_error(f'Error filling form for {username}: {str(e)}')

fill_form()