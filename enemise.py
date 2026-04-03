class Gobline:
    def __init__(self,name,damage,hp) ->None:
        self.name = name
        self.damage = damage
        self.hp = hp
    
    def attack(self,target):
        print(f"Goblin {self.name} attacks {target.name}")
        target.hp -= self.damage

    def __str__(self)->str:
        return f"Name{self.name}\n\tDamage: {self.damage}\n\tHealth:{self.hp}"

class Vampire:
    def __init__(self,name,damage,hp) ->None:
        self.name = name
        self.damage = damage
        self.hp = hp
    
    def attack(self,target):
        print(f"Vampire {self.name} attacks {target.name}")
        target.hp -= self.damage

    def light_steal(self,target):
        print(f"Vampire {self.name} steald hp from {target.name}")
        target.hp -=5
        self.hp+=5

    def __str__(self)->str:
        return f"Name{self.name}\n\tDamage: {self.damage}\n\tHealth:{self.hp}"