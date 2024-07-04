import random

class Field:
    def __init__(self, name):
        self.name = name
        self.field_type = None #self.field_type初始化为None，表示尚未选择特定的字段类型。
        
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
        # Castle Walls have no effect
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
            print(combatant.details())  # 假设details()方法在Combatant类中定义
    
    def restoreCombatants(self):
        for combatant in self.combatants:
            combatant.restore()  # 假设在Combatant类中定义了restore()方法
    
    def duel(self, combatant1, combatant2):
        if combatant1 in self.combatants and combatant2 in self.combatants:
            round_count = 0
            while round_count < 10 and combatant1.isAlive() and combatant2.isAlive():
                self.field.applyFieldEffect(combatant1, combatant2)
                combatant1.attack(combatant2)
                if combatant2.isAlive():  # 检查战士1攻击后战士2是否还活着
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
class Combatant:
    def __init__(self, name, combat_class, health, defense):
        self.name = name
        self.combat_class = combat_class
        self.max_health = health
        self.current_health = health
        self.defense = defense
    
    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.current_health = max(self.current_health - actual_damage, 0)
        if self.current_health == 0:
            return f"{self.name} has been knocked out!"
        return f"{self.name} takes {actual_damage} damage!"

    def reset(self):
        self.current_health = self.max_health
    
    def details(self):
        return f"Name: {self.name}, Class: {self.combat_class}, Health: {self.current_health}/{self.max_health}, Defense: {self.defense}"
class Mage(Combatant):
    def __init__(self, name, combat_class, health, defense, mana, magic_level):
        super().__init__(name, combat_class, health, defense)
        self.mana = mana
        self.magic_level = magic_level
        self.regen_rate = magic_level / 4
    
    def cast_spell(self):
        raise NotImplementedError("The cast_spell method must be implemented in subclasses.")
    
    def reset_values(self):
        super().reset()
        self.mana = self.magic_level
    
    def details(self):
        base_details = super().details()
        return f"{base_details}, Mana: {self.mana}, Magic Level: {self.magic_level}"
class PyroMage:
    def __init__(self, strength_level, flame_boost, mana, regen_value):
        self.strength_level = strength_level
        self.flame_boost = flame_boost
        self.mana = mana
        self.regen_value = regen_value

    def cast_superheat(self):
        if self.mana >= 40:
            self.flame_boost += 1
            self.mana -= 40
            self.regen_mana()

    def cast_fireblast(self):
        if 10 < self.mana < 40:
            self.mana -= 10
            self.regen_mana()

    def regen_mana(self):
        self.mana += self.regen_value

    def calculate_damage(self):
        bonus_damage = 0  # Placeholder for any additional bonuses
        return (self.strength_level * self.flame_boost) + bonus_damage


class FrostMage:
    def __init__(self, magic_level, ice_block, mana, regen_value):
        self.magic_level = magic_level
        self.ice_block = ice_block
        self.mana = mana
        self.regen_value = regen_value

    def cast_ice_block(self):
        if self.mana >= 50:
            self.ice_block = True
            self.mana -= 50
            self.regen_mana()

    def cast_ice_barrage(self):
        if 10 < self.mana < 50:
            self.mana -= 10
            self.regen_mana()

    def regen_mana(self):
        self.mana += self.regen_value

    def calculate_damage(self):
        bonus_damage = 0  # Placeholder for any additional bonuses
        return (self.magic_level / 4) + bonus_damage
class Ranger:
    def __init__(self):
        self.arrows = 3
    
    def fire_arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.arrows == 0:
                print("Last arrow fired!")
        else:
            print("No arrows left!")
    
    def reset(self):
        self.arrows = 3
    
    def calculate_damage(self, ranged_level, strength_level):
        if self.arrows > 0:
            return ranged_level
        else:
            return strength_level


class Warrior:
    def __init__(self):
        self.armour_value = 10
    
    def take_damage(self, amount):
        self.armour_value -= amount
        if self.armour_value <= 0:
            print("Armour shattered!")
            self.armour_value = 0
    
    def reset(self):
        self.armour_value = 10
    
    def calculate_power(self, strength_level):
        return strength_level


class Dharok(Warrior):
    def __init__(self):
        super().__init__()
    
    def calculate_power(self, strength_level, current_health, max_health):
        missing_health = max_health - current_health
        bonus_damage = missing_health
        return strength_level + bonus_damage


class Guthans(Warrior):
    def __init__(self):
        super().__init__()
    
    def calculate_power(self, strength_level):
        self.heal()
        return strength_level
    
    def heal(self):
        print("Healing based on strength level / 5")
        # Implement healing logic here


class Karil(Warrior):
    def __init__(self, ranged_level):
        super().__init__()
        self.ranged_level = ranged_level
    
    def calculate_power(self, strength_level):
        return strength_level + self.ranged_level


### Testing

# Create instances of each class
ranger = Ranger()
warrior = Warrior()
dharok = Dharok()
guthans = Guthans()
karil = Karil(ranged_level=5)

# Test cases for Ranger
print("--- Testing Ranger ---")
ranger.fire_arrow()  # Should decrement arrows
ranger.fire_arrow()
ranger.fire_arrow()
ranger.fire_arrow()  # Should print "Last arrow fired!"
ranger.reset()  # Reset arrows to 3
print()

# Test cases for Warrior
print("--- Testing Warrior ---")
warrior.take_damage(5)
warrior.take_damage(5)  # Should print "Armour shattered!"
warrior.reset()  # Reset armour to 10
print()

# Test cases for Dharok
print("--- Testing Dharok ---")
print("Dharok's power with 100 strength, 50 current health, 100 max health:", dharok.calculate_power(100, 50, 100))
print()

# Test cases for Guthans
print("--- Testing Guthans ---")
print("Guthans's power with 80 strength:", guthans.calculate_power(80))
print()

# Test cases for Karil
print("--- Testing Karil ---")
print("Karil's power with 90 strength:", karil.calculate_power(90))
