class Hero:
    def init(self, name, last_name, lor, history, old, weaknesses, spells, speed, intelligence, power, agility, lucky, power_damage, exp):
        self.lvl  = 1 #Уровень,
        self.name = name #имя,
        self.last_name = last_name # прозвище,
        self.lor = lor #происхождение;
        self.history = history #Принадлежность,
        self.hp = 50 #Здоровье,
        self.old = old #возраст,
        self.spells = spells #Умения и способности,
        self.radius = 50 #Радиус поражения/атаки,
        self.weaknesses = weaknesses #Слабые стороны(список, словарь),
        self.gender = None #ПОЛ??
        self.attr = {'speed':speed,  #Скорость,
                     'intelligence': intelligence, #интеллект,
                     'power':power,  #сила,
                     'agility':agility, #ловкость,
                     'lucky':lucky,  #удача,
                     'power_damage':power_damage, #сила атаки,
                     'exp':exp #опыт,
                    }
    def atack_to_damage(self): #Атака персонажа
        pass
    def protection_to_damage(self): #Защита персонажа
        pass
