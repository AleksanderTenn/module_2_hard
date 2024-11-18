import random
number_one=random.randint(3,20)
print('number_one = ', number_one)
password = []
for i in range(1, number_one):
    for j in range(i+1, number_one):
        if number_one%(i+j)==0:
                 password.extend([i,j])
print('пароль: ',*password)
