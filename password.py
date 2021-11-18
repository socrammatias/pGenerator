import random
import string

x = 0 
password = ""

for x in range(1, 20): # se voce quiser trocar a quantidade de caracteres aumente ou diminue o range
    i = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
    password += i

print(password)





