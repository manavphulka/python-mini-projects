import random
import string
import pyperclip

# ::: USER INPUT :::
pas = int(input("\nHow long should your password be? → "))
print("\n")

# ::: CHARACTER POOL :::
pool = string.ascii_letters + string.digits #+ string.punctuation

# ::: RANDOM CHOICE :::
random.choice(pool)

# ::: LOOP :::
password = ""
for i in range(pas):
    char = random.choice(pool)
    password += char
    

print(password,"\n\n")
pyperclip.copy(password)
print("Password copied to clipboard!")
