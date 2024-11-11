class Log:
    #Основные параметры для отслеживания
    def __init__(self, lvl, name):
        self.lvl = lvl
        #Создание и перезапись файла для каждого цикла игры
        with open('log.txt', 'w') as f:
            f.write(f'{name} - Новый герой!')

    #Отображение урона по персонажу
    def damage(self, name, damage_hero):
        println = f'{name} Нанес {damage_hero} урона'
        #Вывод в консоль
        print(println)
        #Запись в файл
        with open('log.txt','a') as f:
            f.write(println)
    pass