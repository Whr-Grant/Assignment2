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
strength = 100
current_health = 50
max_health = 100
print(f"Dharok's power with {strength} strength, {current_health} current health, {max_health} max health:", dharok.calculate_power(strength, current_health, max_health))
print()

# Test cases for Guthans
print("--- Testing Guthans ---")
strength = 80
print(f"Guthans's power with {strength} strength:", guthans.calculate_power(strength))
print()

# Test cases for Karil
print("--- Testing Karil ---")
strength = 90
print(f"Karil's power with {strength} strength:", karil.calculate_power(strength))
