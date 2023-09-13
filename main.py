import random
from cryptography.fernet import Fernet
# characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# capital_characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '<', '>', '?', '|', '/']
# numbers = ["0","1","2","3","4","5","6","7","8","9",]
#
# password_char = [random.choice(characters)]
# print(password_char)



capitals = int(input("How many upper case characters?:"))
lowercase = int(input("How many lower case characters?:"))
nums = int(input("How many digits?:"))
special_char = int(input("How many Special Characters?:"))

passwordBuild = []

for c in range(capitals):
    cap_pass = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    passwordBuild.append(cap_pass)
for l in range(lowercase):
    low_pass = random.choice("abcdefghijklmnopqrstuvwxyz")
    passwordBuild.append(low_pass)
for n in range(nums):
    num_pass = random.choice("0123456789")
    passwordBuild.append(num_pass)
for s in range(special_char):
    schar_pass = random.choice("!@:;#$%^&*,<>?|/")
    passwordBuild.append(schar_pass)

random.shuffle(passwordBuild)
password = "".join(passwordBuild)
print("Your random password is:", password)

#makes a key
key = Fernet.generate_key()
crypter = Fernet(key)

#encrypts/encodes password
pw = crypter.encrypt(password.encode())
#decrypts password
decrypter = crypter.decrypt(pw)

# print(str(pw, 'utf8'))
# print(str(decrypter, 'utf8'))
#prints the encrypted password
print("this password encrypted is:", pw)
#prints and decodes the decrypted password
print("this password decrypted is:",decrypter.decode())