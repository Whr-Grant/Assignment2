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
