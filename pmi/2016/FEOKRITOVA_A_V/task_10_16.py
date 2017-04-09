balance = 30 
person = {'Сила':'0','Здоровье':'0','Мудрость':'0','Ловкость':'0'}
points = 0 
choice = None 

print('''
                     Добро пожаловать!
            Вы запустили "Генератор персонажей"
          Вам предоставлено 30 пунктов, которые вы 
        можете распределить между 4 характеристиками.
  ''')
	
while choice != '0' :
	print(
	'''
	
	0-Выйти
	1-Показать характеристики
	2-Добавить пункт в характеристики
	3-Уменьшить пукт в характеристики
	
	''')
	
    choice=input('Ваш выбор:')
    print()
	
 #выход
 if choice == '0' :
	print('До свидания.')	
		
 #Вывод на экран характеристик
 elif choice == '1' :
		print('\nХарактеристики:\n')
        for item in person :
            if (item == 'Ловкость') or (item == 'Мудрость') or (item == 'Здоровье') :
              print(item, " | ", person[item])
             else :
              print(item, "\t  | ", person[item])
			  
 #Добавление пунктов в характеристиках
 elif choice == '2' :
        print('Пожалуйста, введите характеристику, в которую хотите добавить пунктов. \nДля изменения доступны', len(person), 'характеристики:\n')
        for item in person :
            print(item)
        char = str(input('\n:'))
        char = char.title()
        while char in person :
            print('\nВведите количество пунктов для этой характеристики. У вас есть', balance, 'свободных пунктов')
            points = int(input('\n:'))
            while (points > balance) or (points < 0) :  
                print('Вы не можете назначить такое количество пунктов. \nВам доступно', balance, 'свободных пунктов')
                points = int(input("\n:"))
        person[char] = points
        print(points, 'пунктов было добавлено к', char)
        balance -= points 	
		
 #Удаление пунктов в характеристиках
 elif choice == '3' :
        print('Пожалуйста, введите имя характеристики для снятия пунктов.', 'Доступно изменение для: ')
        for item in person:
            if int(person[item]) > 0 : 
                print(item)
        char = str(input('\n:'))
        char = char.title()
        while char in person :
            print('\nВведите количество пунктов для характеристики. Доступно', person[char], 'пунктов:')
            points = int(input("\n:"))
            while (points > int(person[char])) or (points < 0) : 
                print('Невозможно удалить такое количество пунктов. Доступно', person[char], 'пунктов')
                points = int(input('\n:'))
        person[char] = points
        print(points, 'пунктов было удалено')
        balance += points		
		
 #Непонятный пользовательский ввод
 else :
		print('Извините, в меню нет пункта', choice)