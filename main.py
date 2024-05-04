import os
from dotenv import load_dotenv
from account import initialize_account
import sys


load_dotenv()

CORRECT_ACCOUNT_ADDRESS = os.getenv("CORRECT_ACCOUNT")
mnemonic = os.getenv("MNEMONIC")


def mnemonic_to_list(mnemonic: str) -> list:
    return mnemonic.split(" ")


def list_to_mnemonic(word_list: list) -> str:
    return " ".join(word_list)


if not mnemonic:
    print("No mnemonic found in .env file. Enter the mnemonic:")
    mnemonic = input()

mnemonic = mnemonic_to_list(mnemonic)


with open("word_list.txt", "r") as f:
    WORD_LIST = f.read().split("\n")

if not WORD_LIST:
    print(
        "No word list found. Please make sure word_list.txt is in the same directory as this script."
    )
    exit()

if not CORRECT_ACCOUNT_ADDRESS:
    print(
        "No correct account address found in .env file. Please enter the correct account address:"
    )
    CORRECT_ACCOUNT_ADDRESS = input()


if not len(mnemonic) == 24:
    print("Invalid mnemonic. Please enter a valid mnemonic.")
    exit()

for i, word in enumerate(mnemonic):
    if word not in WORD_LIST:
        print("Invalid mnemonic. Please enter a valid mnemonic.")
        exit()

    for list_word in WORD_LIST:
        altered_mnemonic = mnemonic.copy()
        altered_mnemonic[i] = list_word

        for index in range(10):
            try:
                account = initialize_account(list_to_mnemonic(altered_mnemonic), index)
                print(f"Account address: {account['account_address'].address_string()}")
            except:
                continue

            if account["account_address"].address_string() == CORRECT_ACCOUNT_ADDRESS:
                print(f"Correct mnemonic: {list_to_mnemonic(altered_mnemonic)}")
                exit()

print("Mnemonic not found.")
