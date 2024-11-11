from heroes import Hero
import config
from enemy import Enemy
from log import Log
import random




def menu():

        ListTextMenu= [
            "Привет, дорогой друг! Добро пожаловать в нашу игру!"
            "Желаю тебе приятно провести время!",
            "Всего у нас 4 игровых персонажа: \n 1. Маг \n 2. Танк \n 3. Воин \n 4. Лучник"
        ]
        print(*ListTextMenu, sep='\n')
        change_user = int(input('Введите число, своего класса:'))
        #Задача спросить у пользователя все параметры для передачи
        name = input('Введите имя персонажа: ')
        last_name = input('Введите прозвище персонажа: ')
        lor = input('Введите лор персонажа: ')
        history = input('Введите история персонажа: ')
        old = input('Введите возраст персонажа: ')
        weaknesses = input('Введите страхи персонажа: ')
        battler(change_user, name, last_name, lor, history, old, weaknesses)

def battler(change_user, name, last_name, lor, history, old, weaknesses):
    hero_class = {}
    if change_user == 1:
        hero_class = config.mage
    elif change_user == 2:
        hero_class = config.tank
    elif change_user == 3:
        hero_class = config.warrior
    elif change_user == 4:
        hero_class = config.archer

    hero = Hero( name, last_name, lor, history, old, weaknesses,*hero_class)
    log = Log( 1, name)
    enemy = Enemy(config.slime)
    hero_damage_menu_battle(hero, enemy)



def hero_damage_menu_battle(hero, enemy, log):
    counter_lvl = 1
    enemy_list =['slime','goblin','spectator','orc']
    while True:
        if enemy.attr['hp'] == 0:
            counter_lvl += 1
            log.victory_lvl()
            en = random.randint(0,3)
            enemy = Enemy(config.enemy_list[en])
        elif enemy.hp == 0:
            log.faild_lvl()
            break
        else:
            enemy.protection_to_damage(hero.atack_to_damage() ) #урон по врагу
            log.damage(enemy.name, hero.atack_to_damage()) #Отображение урона на экране
            hero.protection_to_damage(enemy.atack_to_damage() ) #Урон по герою
            log.damage(hero.name, enemy.atack_to_damage()) #Отображение урона на экране
    print('Game OVER!')
