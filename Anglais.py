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
               "Il est": "He is",
               "Elle est": "She is",
               "On est": "it is",
               "Nous sommes": "We are",
               "Vous êtes" : "You are",
                  "Ils sont": "They are",
                  "Elles sont": "They are"}.items())

VERBS_HAVE = tuple({"j'ai": "I have",
                    "Tu as": "You have",
                    "Il est": "He has",
                    "Elle est" : "She has",
                    "On est" : "It has",
                    "Nous avons" : "We have",
                    "Vous avez" : "You have",
                    "Ils sont": "They have",
                    "Elles sont": "They have"}.items())

NATURE = tuple({"ajouter": "add",
                "répondre" : "answer",
                "zone, région" : "area",
                "croire" : "believe",
                "oiseau" : "bird",
                "souffler" : "blow",
                "réserver" : "book up",
                "buisson" : "bush",
                "charmant" : "charming",
                "poussin" : "chick"}.items())


def main_menu():
    print()
    print()
    print("1.  Français --> Anglais")
    print()
    print("2.  Anglais --> Français")
    print()
    print("3.  Conjugaison du Verbe  être (Français --> Anglais)")
    print()
    print("4.  Conjugaison du Verbe  être (Anglais --> Français)")
    print()
    print("5.  Conjugaison du Verbe avoir (Français --> Anglais)")
    print()
    print("6.  Conjugaison du Verbe avoir (Français --> Anglais)")
    print()
    return input("Quel est ton choix :")




def ask(word_to_translate, translated_word):
    answer = input("Quel est la traduction de {} :".format(word_to_translate))
    
    if answer.lower().strip() == translated_word.lower():
        print("Bonne réponse !")
    else:
        print("Non, c'est {}".format(translated_word))



def main(choice, runs=16):

    for _ in range(runs):
        
        if int(choice) == 1:
            word_to_translate, translated_word = random.choice(WORDS)
        if int(choice) == 2:
            translated_word, word_to_translate = random.choice(WORDS)
        if int(choice) == 3:
            word_to_translate, translated_word = random.choice(VERBS_BE)
        if int(choice) == 4:
            translated_word, word_to_translate = random.choice(VERBS_BE)
        if int(choice) == 5:
            word_to_translate, translated_word = random.choice(VERBS_HAVE)
        if int(choice) == 6:
            translated_word, word_to_translate = random.choice(VERBS_HAVE)
    
        ask(word_to_translate, translated_word)

       
        
        
            




if __name__ == '__main__':
    main(main_menu())
