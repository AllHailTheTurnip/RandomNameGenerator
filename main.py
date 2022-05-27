import random


def randomName():
    length = random.randint(3, 12)
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    name = ""
    vowelNext = random.randint(0, 1) == 1
    for x in range(0, length):
        if vowelNext is True:
            name += vowels[random.randint(0, len(vowels)-1)]
        else:
            name += consonants[random.randint(0, len(consonants)-1)]
        if random.randint(0, 20) != 20:
            vowelNext = not vowelNext
    name = name.capitalize()
    return name