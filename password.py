t =  """___________    ______ ________  _  _____________  __| _/
\____ \__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ | 
|  |_> > __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ | 
|   __(____  /____  >____  >  \/\_/ \____/|__|  \____ | 
|__|       \/     \/     \/                          \/  By: tarkerin           
"""
import random
import string
print(t)
x = 0 
password = ""
y = input('Você deseja gerar uma senha? S/N ')
if y == 'S':
    qtd = int(input('Digite a quantidade de caracteres que você deseja na sua senha: '))
else:
    exit()

for x in range(qtd):
    i = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
    password += i

print(password)





