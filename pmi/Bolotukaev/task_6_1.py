# Задача 6. Вариант 1. 
# Создайте игру, в которой компьютер загадывает название
#одного из трех мушкетеров д'Артаньяна, а игрок должен его угадать.


# Bolatukaev A.Z. 
# 20.03.2017


import random
a = ('Атос' , 'Портос', 'Арамис')
b = (random.choice(a))
ans = input ("Попробуйте угадать одного из трех мушкетеров д'Артаньяна:")
if ans == b:
    print ("Поздравляю, это правильный ответ!!!")
else:
    print ("Ты не угадал((")
input ()
