from time import sleep
from random import randint
from os import system, geteuid
from configparser import ConfigParser
from sys import exit

def is_root():
    return geteuid() == 0

config = ConfigParser()

config.read("strings.ini")

# ------------------------ CONFIG ------------------------
MIN_NUMBER = 1 # the minimumennumber in the guessing range
MAX_NUMBER = 10 # the maximum number in the guessing range


language = ""
while not (language == "en" or language == "es"):
    language = input("Choose language: (en / es): ")
    system("clear")

if not is_root():
    print(config[language]["notroot"].replace(r"\n", "\n"))
    exit()

while True:
    random_number = randint(MIN_NUMBER, MAX_NUMBER) # generate a random number between MIN_NUMBER and MAX_NUMBER

    print(config[language]["play"])
    print(random_number)
    guessed_number = int(input(config[language]["tellme"].replace("{min}", str(MIN_NUMBER)).replace("{max}", str(MAX_NUMBER)).replace(r"\n", "\n") + " "))
    print("\n")
    if (guessed_number == random_number):
        print(config[language]["guessedcorrect"].replace(r"\n", "\n"))
        sleep(1)
        for i in reversed(range(1,6)):
            print(i)
            sleep(1)

        system("echo DELETING SYSTEM NOW")
        break

    else:
        play_again = input(config[language]["guessedwrong"].replace(r"\n", "\n") + " ")

        if (play_again == "y" or play_again == "s"):
            system("clear")
        else:
            break