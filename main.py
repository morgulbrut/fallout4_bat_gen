__author__ = 't800'

import re

ids = []

with open('perks_i.txt') as file:
    text = file.read()
    textlist = text.split('|')
    for element in textlist:
        if re.search(r"[0-9]([0-9]*[A-F]*[a-f]*)*}}", element):
            ids.append(re.match(r"([0-9]*[A-F]*[a-f]*)*", element).group())

with open('perks.txt', 'w') as file:
    for element in ids:
        file.write('player.addperk ' + element + '\n')

ids = []

with open('ammo_i.txt') as file:
    text = file.read()
    textlist = text.split('|')
    for element in textlist:
        if re.search(r"[0-9]([0-9]*[A-F]*[a-f]*)*}}", element):
            ids.append(re.match(r"([0-9]*[A-F]*[a-f]*)*", element).group())

with open('ammo.txt', 'w') as file:
    for element in ids:
        file.write('player.additem ' + element + ' 1000\n')

ids = []

with open('explosives_i.txt') as file:
    text = file.read()
    textlist = text.split('|')
    for element in textlist:
        if re.search(r"[0-9]([0-9]*[A-F]*[a-f]*)*}}", element):
            ids.append(re.match(r"([0-9]*[A-F]*[a-f]*)*", element).group())

with open('explosives.txt', 'w') as file:
    for element in ids:
        print(element)
        file.write('player.additem ' + element + ' 25\n')
