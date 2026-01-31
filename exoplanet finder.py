import time

def scan_exoplanet(planet_name, temperature, has_water, has_oxygen):
    print(f"Scanning {planet_name} for life markers...")
    time.sleep(1)

    if 273 < temperature < 373 and has_water and has_oxygen:
        return True
    return False

targets = [
    {"name" : "Kepler-452b", "temp" : 265, "water" : True, "oxygen" : False},
    {"name" : "Proxima B", "temp" : 300, "water" : True, "oxygen" : True},
    {"name" : "Mars", "temp" : 210, "water" : False, "oxygen" : False}
]

for planet in targets:
    found = scan_exoplanet(planet['name'], planet['temp'], planet['water'], planet['oxygen'])
    if found:
        print(f"!!! SIGNAL DETECTED: Life potential on {planet['name']} !!!")
    else:
        print(f"No signal from {planet['name']}.")