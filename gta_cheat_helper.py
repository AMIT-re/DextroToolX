import pydirectinput
import keyboard
import time

def type_cheat(cheat_code):
    print(f"Typing cheat: {cheat_code}")
    pydirectinput.write(cheat_code)  # Type the entire cheat code at once
    pydirectinput.press('enter')  # Press Enter key after typing the cheat code

# Hotkey to trigger cheat codes with a delay
keyboard.add_hotkey('ctrl+shift+g', lambda: [time.sleep(0.5), type_cheat('toolup')])          # Weapons
keyboard.add_hotkey('ctrl+shift+h', lambda: [time.sleep(0.5), type_cheat('turtle')])          # Health & Armor
keyboard.add_hotkey('ctrl+shift+e', lambda: [time.sleep(0.5), type_cheat('highex')])          # Explosive ammo
keyboard.add_hotkey('ctrl+shift+b', lambda: [time.sleep(0.5), type_cheat('painkiller')])      # Invincibility
keyboard.add_hotkey('ctrl+shift+n', lambda: [time.sleep(0.5), type_cheat('thugstools')])      # Weapons & Ammo
keyboard.add_hotkey('ctrl+shift+m', lambda: [time.sleep(0.5), type_cheat('professionalkit')]) # Special Ability Recharge
keyboard.add_hotkey('ctrl+shift+k', lambda: [time.sleep(0.5), type_cheat('turtlebomb')])      # Explosive Melee Attacks
keyboard.add_hotkey('ctrl+shift+l', lambda: [time.sleep(0.5), type_cheat('hothands')])        # Flaming Bullets
keyboard.add_hotkey('ctrl+shift+p', lambda: [time.sleep(0.5), type_cheat('incendiary')])      # Incendiary Bullets
keyboard.add_hotkey('ctrl+shift+o', lambda: [time.sleep(0.5), type_cheat('liquor')])          # Drunk Mode
keyboard.add_hotkey('ctrl+shift+i', lambda: [time.sleep(0.5), type_cheat('fugitive')])        # Wanted Level Up
keyboard.add_hotkey('ctrl+shift+u', lambda: [time.sleep(0.5), type_cheat('lawyerup')])        # Wanted Level Down
keyboard.add_hotkey('ctrl+shift+y', lambda: [time.sleep(0.5), type_cheat('catchme')])         # Slippery Cars
keyboard.add_hotkey('ctrl+shift+t', lambda: [time.sleep(0.5), type_cheat('offroad')])         # Jumping Cars
keyboard.add_hotkey('ctrl+shift+r', lambda: [time.sleep(0.5), type_cheat('floater')])         # Moon Gravity
keyboard.add_hotkey('ctrl+shift+f', lambda: [time.sleep(0.5), type_cheat('hoptoit')])         # Super Jump
keyboard.add_hotkey('ctrl+shift+v', lambda: [time.sleep(0.5), type_cheat('skydive')])         # Skyfall
keyboard.add_hotkey('ctrl+shift+c', lambda: [time.sleep(0.5), type_cheat('bandit')])          # Spawn Buzzard Attack Helicopter
keyboard.add_hotkey('ctrl+shift+x', lambda: [time.sleep(0.5), type_cheat('comet')])           # Spawn Comet
keyboard.add_hotkey('ctrl+shift+z', lambda: [time.sleep(0.5), type_cheat('rapidgt')])         # Spawn Rapid GT
keyboard.add_hotkey('ctrl+shift+a', lambda: [time.sleep(0.5), type_cheat('trashmaster')])     # Spawn Trashmaster
keyboard.add_hotkey('ctrl+shift+s', lambda: [time.sleep(0.5), type_cheat('limousine')])       # Spawn Limousine
keyboard.add_hotkey('ctrl+shift+d', lambda: [time.sleep(0.5), type_cheat('barnstorm')])       # Spawn Duster
keyboard.add_hotkey('ctrl+shift+q', lambda: [time.sleep(0.5), type_cheat('pocketrocket')])    # Spawn Sanchez
keyboard.add_hotkey('ctrl+shift+w', lambda: [time.sleep(0.5), type_cheat('stuntplane')])      # Spawn Stunt Plane

print("✅ GTA V Cheat Helper Running...")
print("🎮 Switch to GTA V and press Ctrl + Shift + [G/H/E/B/N/M/K/L/P/O/I/U/Y/T/R/F/V/C/X/Z/A/S/D/Q/W]")
print("❌ Press F12 to exit")

keyboard.wait('F12')
