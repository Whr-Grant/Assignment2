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
