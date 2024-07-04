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
