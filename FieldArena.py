import random

class Field:
    def __init__(self, name):
        self.name = name
        self.field_type = None
    
    def changeField(self):
        # 随机选择三种字段类型中的一种
        field_types = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]
        self.field_type = random.choice(field_types)
    
    def applyFieldEffect(self, combatant1, combatant2):
        if self.field_type == "Toxic Wasteland":
            combatant1.takeDamage(5)
            combatant2.takeDamage(5)
        elif self.field_type == "Healing Meadows":
            combatant1.heal(5)
            combatant2.heal(5)
        # Castle Walls 没有效果

class Arena:
    def __init__(self, field):
        self.combatants = []
        self.field = field
    
    def addCombatant(self, combatant):
        if combatant not in self.combatants:
            self.combatants.append(combatant)
        else:
            print(f"{combatant.name} is already in the arena.")
    
    def removeCombatant(self, combatant):
        if combatant in self.combatants:
            self.combatants.remove(combatant)
        else:
            print(f"{combatant.name} is not in the arena.")
    
    def listCombatants(self):
        for combatant in self.combatants:
            if hasattr(combatant, 'details') and callable(getattr(combatant, 'details')):
                print(combatant.details())  # Assuming details() method is defined in Combatant class
            else:
                print(f"{combatant.name} is missing details() method.")
    
    def restoreCombatants(self):
        for combatant in self.combatants:
            if hasattr(combatant, 'restore') and callable(getattr(combatant, 'restore')):
                combatant.restore()  # Assuming restore() method is defined in Combatant class
            else:
                print(f"{combatant.name} is missing restore() method.")
    
    def duel(self, combatant1, combatant2):
        if combatant1 in self.combatants and combatant2 in self.combatants:
            round_count = 0
            while round_count < 10 and combatant1.isAlive() and combatant2.isAlive():
                self.field.applyFieldEffect(combatant1, combatant2)
                combatant1.attack(combatant2)
                if combatant2.isAlive():
                    combatant2.attack(combatant1)
                round_count += 1
            if not combatant1.isAlive():
                print(f"{combatant2.name} wins!")
            elif not combatant2.isAlive():
                print(f"{combatant1.name} wins!")
            else:
                print("The duel ended in a draw after 10 rounds.")
        else:
            print("Invalid combatants for duel or combatants are not in the arena.")

