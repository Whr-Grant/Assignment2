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
