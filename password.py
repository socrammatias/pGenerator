import random
import string

x = 0 
password = ""
qtd = int(input('Digite a quantidade de caracteres que você deseja na sua senha: '))

for x in range(qtd):
    i = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
    password += i

print(password)





