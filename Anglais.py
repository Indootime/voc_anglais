


#!/usr/bin/env python3

import random

WORDS = tuple({"Rouge": "Red",
               "Vert": "Green",
               "Bleu": "Blue",
               "Jaune": "Yellow",
               "Soleil": "Sun",
               "Lundi": "Monday",
               "Mardi": "Tuesday",
               "Mercredi": "Wednesday",
               "Jeudi": "Thursday",
               "Vendredi": "Friday",
               "Samedi": "Saturday",
               "Dimanche": "Sunday",
               "Demain": "Tomorrow",
               "Hier": "Yesterday",
               "Aujourd'hui": "Today",
               "être": "Be",
               "Avoir": "Have"}.items())


def main_menu():
    print("1.  Anglais --> Français")
    print()
    print("2.  Français --> Anglais")
    print()
    return input("Quel est ton choix :")


def ask(word_to_translate, translated_word):
    answer = input("Quel est la traduction de {} :".format(word_to_translate))
    if answer.lower() == translated_word.lower():
        print("Bonne réponse !")
        
    else:
        print("Non, c'est {}".format(translated_word))

def main(choice, runs=15):
    for _ in range(runs):
        if int(choice) == 1:
            word_to_translate, translated_word = random.choice(WORDS)
        else:
            translated_word, word_to_translate = random.choice(WORDS)
        ask(word_to_translate, translated_word)




if __name__ == '__main__':
    main(main_menu())
