import time
import random

time.sleep(1)

def guessing():
    password = random.randint(1, 2)
    while True:
        login = input("put in the password. if you get it correct you login.\n")
        if login == str(password):
            print("congrats you've logged in!")
            break
        else:
            Retry = input("\nWrong. Do you want to try again?\n Y for yes ||| N for no\n")
            if Retry.lower() not in ["y", "yes"]:
                break

