import game
from heroes import Hero
import config

def main():
    hero = Hero(1, "name", 'lor', 'history',25,17,config.mage_spells,10,'',config.mage)
    game.menu()
    game.battler()





if __name__ == 'main':
    main()