# The purpose of this project is to generate a random name based on two lists.
import sys, random

# Decided to use tuples as container since updates to the lists wont be required
# List of Colors and list of common house plant names to create a 'Plant Alias'
colors=('Green', 'Blue', 'Yellow', 'Red', 'Orange', 'Purple',
        'Brown', 'White', 'Black', 'Cyan', 'Magenta',
        'Lilac', 'Lime', 'Pink')
plant_names=('Fern', 'Evergreen', 'Monstera', 'Maranta', 'Pothos',
             'Fig', 'Chestnut', 'Alocasia', 'Yucca', 'Perperomia',
             'Lily', 'Aloe', 'Ivy', 'Anthurium', 'Calathea', 'Croton',
             'Jade', 'Staghorn', 'Orchid', 'Begonia')


# Start intro of application
print('Welcome to the Plant Alias name generator!')
# Start loop to randomly choose a color for a first name and a plant name for a last name

while True:
    first = random.choice(colors)
    last = random.choice(plant_names)

    print('\n\n')
    print('An Alias is being created...')

    print('\n\n')
    print('Your new Alias is: {} {}'.format(first, last), file=sys.stderr)
    print('\n\n')

    try_again = input('Would you like a different Plant Alias? (y/n)')
    if try_again.lower() == 'n':
        break

input('\nPress Enter to exit.')

