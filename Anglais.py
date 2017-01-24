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

VERBS_BE = tuple({"Je suis": "I am",
               "Tu es": "You are",
               "Il est": "It is",
               "Elle est": "She is",
               "On est": "He is",
               "Nous sommes": "We are",
               "Vous êtes" : "You are",
               "Ils,Elle sont": "They are"}.items())

VERBS_HAVE = tuple({"j'ai": "I have",
                    "Tu as": "You have",
                    "Il est": "It has",
                    "Elle est" : "She has",
                    "On est" : "He has",
                    "Nous avons" : "We have",
                    "Vous avez" : "You have",
                    "Ils, Elles sont": "They have"}.items())



def main_menu():
    print("1.  Anglais --> Français")
    print()
    print("2.  Français --> Anglais")
    print()
    print("3.  Conjugaison du Verbe  être")
    print()
    print("4.  Conjugaison du Verbe avoir")
    print()
    return input("Quel est ton choix :")


def ask(word_to_translate, translated_word):
    answer = input("Quel est la traduction de {} :".format(word_to_translate))
    
    if answer.lower().strip() == translated_word.lower():
        print("Bonne réponse !")
        
    else:
        print("Non, c'est {}".format(translated_word))

def main(choice, runs=15):
    for _ in range(runs):
        if int(choice) == 1:
            word_to_translate, translated_word = random.choice(WORDS)
        if int(choice) == 2:
            translated_word, word_to_translate = random.choice(WORDS)
        if int(choice) == 3:
            word_to_translate, translated_word = random.choice(VERBS_BE)
        if int(choice) == 4:
            word_to_translate, translated_word = random.choice(VERBS_HAVE)
        ask(word_to_translate, translated_word)
        
            




if __name__ == '__main__':
    main(main_menu())
