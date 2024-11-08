def menu(self):
    pass
def battler(self):
    pass
def hero_damage_menu_battle(self):
    from heroes inport Hero

def menu():

        ListTextMenu= [
            "Привет, дорогой друг! Добро пожаловать в нашу игру!"
            "Желаю тебе приятно провести время!",
            "Всего у нас 4 игровых персонажа: \n 1. Маг \n 2. Танк \n 3. Воин \n 4. Лучник"
        ]
        print(ListTextMenu, sep='\n')
        change_user = int(input('Введите число, своего класса:'))
        battler(change_user)

def battler(change_user) == 1
    hero_class = {}
    if change_user == 1:
        hero_class = config.mage
    elif change_user == 2:
        hero_class = config.tank
    elif change_user == 3:
        hero_class = config.warrior
    elif change_user == 4:
        hero_class = config.archer
