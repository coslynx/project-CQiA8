import threading

def create_discord_account(username, email, password, birthdate):
    # Logic to create a Discord account
    
def multi_threaded_account_creation(num_threads, account_info_list):
    threads = []
    for account_info in account_info_list:
        thread = threading.Thread(target=create_discord_account, args=account_info)
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_threads = 5
    account_info_list = [
        ("user1", "user1@example.com", "password1", "01/01/2000"),
        ("user2", "user2@example.com", "password2", "02/02/2000"),
        ("user3", "user3@example.com", "password3", "03/03/2000"),
        ("user4", "user4@example.com", "password4", "04/04/2000"),
        ("user5", "user5@example.com", "password5", "05/05/2000")
    ]
    
    multi_threaded_account_creation(num_threads, account_info_list)