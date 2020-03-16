from random import choice

aliens = []

colors = ['green', 'blue', 'red', 'yellow', 'pink', 'orange', 'purple', 'black',
'white']

points = [point for point in range(1, 100)]

speed = ['slow', 'medium', 'fast', 'ultrafast']

for alien_num in range(0, 30):
    new_alien = {
        'color': choice(colors),
        'points': choice(points),
        'speed': choice(speed),
    }

    aliens.append(new_alien)

for alien in aliens:
    print(alien)

for alien in aliens:
    if alien['color'] == 'green' and alien['speed'] == 'slow':
        alien['points'] += 10
        print(alien)

print(f"Total number of aliens: {len(aliens)}")