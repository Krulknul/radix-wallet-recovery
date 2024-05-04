# Radix wallet recoverer

### Takes as input:

- faulty 24-word mnemonic for the Radix Babylon mobile wallet
- Account address of the account you're looking for

### What it does:

If your assumption is that only one word of the mnemonic is written down incorrectly, you could try to substitute each word manually for another word in the list, and seeing if it produces the right account address. That's what this script automates. If it finds the mnemonic for the address, it will print it out. If it doesn't, it will print that no mnemonic was found.

### How to use

- Install Python. This project was tested on Python 3.9
- Install the required packages. This can be done using: `pip install -r requirements.txt`
- Either:
  - Copy the env.template file as `.env`, and change the values
  - Run the program without a .env file, and input the values at the prompt.

To run the program: `python3 main.py`
