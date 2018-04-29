#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import random
from tkinter.messagebox import *
from datetime import datetime
from time import sleep
import getpass

user = getpass.getuser()

WORDS1 = tuple({"Rouge": "red",
               "Vert": "green",
               "Bleu": "blue",
               "Jaune":"yellow",
               "noir":"black",
               "beige":"beige",
               "marron":"brown",
               "doré":"golden",
               "mauve":"mauve",
               "bleu marine":"navy blue",
               "rose":"pink",
               "argent":"silver",
               "blanc":"white",
               "gris":"grey",
               "multicolore":"multicolored",
               "sombre":"dark",
               "clair":"light",
               "Lundi": "monday",
               "Mardi": "tuesday",
               "Mercredi": "wednesday",
               "Jeudi": "thursday",
               "Vendredi": "friday",
               "Samedi": "saturday",
               "Dimanche": "sunday",
               "Demain": "tomorrow",
               "Hier": "yesterday",
               "Aujourd'hui": "today",
               "janvier": "january",
               "février": "february",
               "mars": "march",
               "avril":"april",
               "mai":"may",
               "juin":"june",
               "juillet":"july",
               "aout":"august",
               "septembre":"september",
               "octobre":"october",
               "novembre":"november",
               "décembre":"december",
               "printemps":"spring",
               "été":"summer",
               "automne":"autumn",
               "hiver":"winter",
               "":""}.items()) ######################################################
print (len(WORDS1))
WORDS3 = tuple({"joyeux":"joyful",
               "heureux":"happy",
               "enthousiaste":"enthusiastic",
               "optimiste":"optimistic",
               "satisfait":"satisfied",
               "fier":"proud",
               "ému":"touched",
               "excité":"excited",
               "bienveillant":"kindly",
               "surpris":"surprised",
               "amoureux":"in love",
               "passionné":"passionate",
               "plein entrain":"livley",
               "gai":"cheerful",
               "admiratif":"appreciative",
               "glad":"content",
               "enchanté":"delighted",
               "confiant":"confident",
               "apeuré":"afraid",
               "effrayé":"scared",
               "furieux":"furious",
               "triste":"sad",
               "découragé":"discouraged",
               "amer":"bitter",
               "en colère":"angry",
               "las":"weary",
               "choqué":"shocked",
               "agacé":"annoyed",
               "agressif":"agressive",
               "déçu":"disappointed",
               "épuisé":"exhausted",
               "mécontent":"discontented",
               "pessimiste":"pessimistic",
               "irrité":"irritated",
               "jaloux":"jealous",
               "nerveux":"nervous",
               "stressé":"stressed",
               "fatigué":"tired",
               "angoissé":"worried",
               "":""}.items())  ####################################################################"
WORDS4 = tuple({"umbrella":"parapluie",
               "warming":"réchauffement",
               "wave":"vague",
               "weather":"temps",
               "wint":"vent",
               "windbreaker":"coupe-vent",
               "windy":"venteux",
               "answer":"répondre",
               "ask":"demander",
               "blackboard":"tableau",
               "borrow from":"empreinter à",
               "break":"récréation",
               "to look for":"chercher, rechercher",
               "to look after":"s'occuper, prendre soin",
               "to ride":"monter",
               "to hunt":"chasser",
               "to shoot":"tirer, tuer, abattre",
               "to kill":"tuer",
               "to explore unknown territories":"explorer des territoires inconnus",
               "to guide":"guider, orienter",
               "to lead":"mener, diriger",
               "to defend":"défendre",
               "gun":"pistolet",
               "rifle":"fusil",
               "castle":"château",
               "cows":"vaches",
               "bulls":"taureaux",
               "calves":"veaux",
               "horses":"chevaux",
               "wild animals":"animaux sauvages",
               "fur animals":"animaux à fourrure",
               "unknown":"inconnu",
               "territories":"territoires",
               "from my point of view":"de mon point de vue",
               "to my mind":"à mon avis",
               "in my opinion":"à mon avis",
               "if you ask me":"si tu veux mon avis",
               "i think":"je pense que",
               "you think":"tu pense que",
               "remarkable":"remarquable",
               "great":"grand, beaucoup",
               "fantastic":"fantastique, formidable",
               "essential":"essentiel, indispensable",
               "unbelievable":"incroyable, pas croyable",
               "incomprehensible":"incompréhensible, comprends pas",
               "unthinkable":"impensable",
               "intolerable":"intolérable,inacceptable",
               "afraid":"crains que",
               "agree":"accepter",
               "about":"concernant, environ",
               "associate":"associé",
               "because of":"en raison de, à cause de",
               "since":"depuis, depuis que",
               "due to":"en raison de",
               "thanks to":"merci à, grâce à",
               "so":"ainsi",
               "that's why":"c'est pourquoi",
               "as a consequence":"en conséquence",
               "therefore":"donc, par conséquence",
               "as a result":"en conséquence",
               "consequently":"par conséquent",
               "pain":"douleur",
               "feel pain":"avoir mal",
               "suffering":"souffrance",
               "suffer":"souffrir",
               "captivity":"captivité",
               "danger":"risque, danger",
               "to be in danger":"être en danger",
               "to improve conditions":"améliorer les conditions",
               "to prevent abuse":"pour éviter les abus",
               "to promote respect":"promouvoir le respect",
               "cruelty":"cruauté",
               "sanctuary":"refuge, sanctuaire",
               "abuse":"abus, violence"}.items())
WORDS5 = tuple({"a few":"quelques",
                "aboard":"à bord",
                "abroad":"à l'étranger",
                "arrière plan":"background",
                "bon marché":"affordable",
                "avoir assez d'argent":"to afford",
                "postuler":"to apply",
                "arrow":"flèche",
                "beautiful":"beau",
                "beetle":"scarabée",
                "navigateur":"browser",
                "bison":"buffalo",
                "menuisier":"carpenter",
                "charrette":"cart",
                "faire du vélo":"to bike",
                "jumelles":"binoculars",
                "naissance":"birth",
                "to cash":"encaisser",
                "cattle":"bétail",
                "cartoon":"bande déssinée",
                "bull":"taureau",
                "faire attention!":"beware!",
                "naufragé":"castaway",
                "clochard":"bum",
                "sang":"blood",
                "livre":"book",
                "channel":"chaîne (télévision)",
                "character":"personnage",
                "bookshop":"librairie",
                "can":"pouvoir",
                "cerise":"cherry",
                "arc":"bow",
                "flambant neuf":"brand new",
                "os":"bone",
                "to bloussom":"fleurir",
                "container":"récipient",
                "dark":"sombre",
                "daylight":"aube, aurore",
                "coach":"entraineur",
                "cloture":"closing",
                "indice":"clue",
                "convaincant":"convincing",
                "coffee":"café",
                "comédie":"comedy",
                "écrevisse":"crawfish",
                "ramper":"to crawl",}.items())
VERBE_IRR = tuple({"arise":"survenir",
    "awake":"se réveiller",
    "be":"être",
    "bear":"porter, supporter",
    "beat":"battre",
    "become":"devenir",
    "begin":"commencer",
    "bend":"se courber",
    "bet":"parier",
    "bind":"lier",
    "bite":"mordre",
    "bleed":"saigner",
    "blow":"souffler",
    "break":"casser",
    "breed":"donner naissance, élever",
    "bring":"apporter",
    "broadcast":"transmettre, émettre",
    "build":"construire",
    "burn":"brûler",
    "burst":"éclater",
    "buy":"acheter",
    "cast":"jeter, projeter",
    "catch":"attraper",
    "choose":"choisir",
    "come":"venir",
    "cost":"coûter",
    "cut":"couper",
    "deal":"distribuer",
    "dig":"creuser",
    "do":"faire",
    "draw":"dessiner",
    "dream":"rêver",
    "drink":"boire",
    "drive":"conduire",
    "eat":"manger",
    "fall":"tomber",
    "feed":"nourrir",
    "feel":"sentir",
    "fight":"combattre",
    "find":"trouver",
    "flee":"fuir",
    "fling":"lancer",
    "fly":"voler",
    "forbid":"interdire",
    "forget":"oublier",
    "forgive":"pardonner",
    "freeze":"geler",
    "get":"obtenir",
    "give":"donner",
    "go":"aller",
    "grow":"pousser",
    "hang":"pendre",
    "have":"avoir",
    "hear":"entendre",
    "hide":"cacher",
    "hit":"frapper",
    "hold":"tenir",
    "hurt":"faire mal",
    "keep":"garder",
      "kneel":"s\'agenouiller",
    "know":"savoir",
    "lay":"placer",
    "lead":"conduire",
    "lean":"s\'appuyer",
    "leap":"sauter",
    "learn":"apprendre",
    "leave":"quitter",
    "lend":"prêter",
    "let":"laisser",
    "lie":"être coucher",
    "light":"allumer",
    "lose":"perdre",
    "make":"faire",
    "mean":"vouloir dire",
    "meet":"rencontrer",
    "mow":"tondre",
    "pay":"payer",
    "put":"mettre",
    "read":"lire",
    "ride":"aller a vélo",
    "ring":"sonner",
    "rise":"se lever",
    "run":"courrir",
    "saw":"scier",
    "say":"dire",
    "see":"voir",
    "seek":"chercher",
    "sell":"vendre",
    "send":"envoyer",
    "set":"placer",
    "sew":"coudre",
    "shake":"secouer",
    "shine":"briller",
    "shoot":"tirer",
    "show":"monter",
    "shrink":"rétrécir",
    "shut":"fermer",
    "sing":"chanter",
    "sink":"s\'enfoncer, couler",
    "sit":"s\'asseoir",
    "sleep":"dormir",
    "slide":"glisser",
    "smell":"sentir",
    "speak":"parler",
    "speed":"se presser",
    "spell":"épeler",
    "spend":"dépenser",
    "spit":"cracher",
    "split":"diviser",
    "spoil":"abîmer ou gâter un enfant",
    "spread":"étaler",
    "spring":"jaillir",
    "stand":"être debout",
    "steal":"voler",
    "stick":"coller",
    "sting":"piquer",
    "stink":"sentir mauvais",
    "stride":"marcher",
    "strike":"frapper",
    "swear":"jurer",
    "sweep":"balayer",
    "swim":"nager",
    "take":"prendre",
    "teach":"enseigner",
    "tear":"déchirer",
    "tell":"dire",
    "think":"penser",
    "throw":"jeter",
    "understand":"comprendre",
    "upset":"troubler",
    "wake":"réveiller",
    "wear":"porter",
    "weep":"pleurer",
    "win":"gagner",
    "write":"écrire"}.items())
VERBE_IRR_PRET= tuple({"arise":"arose",
    "awake":"awoke",
    "be":"was",
    "bear":"bore",
    "beat":"beat",
    "become":"became",
    "begin":"began",
    "bend":"bent",
    "bet":"bet",
    "bind":"bound",
    "bite":"bit",
    "bleed":"bled",
    "blow":"blew",
    "break":"broke",
    "breed":"bred",
    "bring":"brought",
    "broadcast":"broadcast",
    "build":"built",
    "burn":"burn, burned",
    "burst":"burst",
    "buy":"bought",
    "cast":"cast",
    "catch":"caught",
    "choose":"chose",
    "come":"came",
    "cost":"cost",
    "cut":"cut",
    "deal":"dealt",
    "dig":"dug",
    "do":"did",
    "draw":"drew",
    "dream":"dreamt, dreamed",
    "drink":"drank",
    "drive":"drove",
    "eat":"ate",
    "fall":"fell",
    "feed":"fed",
    "feel":"felt",
    "fight":"fought",
    "find":"found",
    "flee":"fled",
    "fling":"flung",
    "fly":"flew",
    "forbid":"forbade",
    "forget":"forgot",
    "forgive":"forgave",
    "freeze":"froze",
    "get":"got",
    "give":"gave",
    "go":"went",
    "grow":"grew",
    "hang":"hung",
    "have":"had",
    "hear":"heard",
    "hide":"hid",
    "hit":"hit",
    "hold":"held",
    "hurt":"hurt",
    "keep":"kept",
    "kneel":"knelt",
    "know":"knew",
    "lay":"laid",
    "lead":"led",
    "lean":"leant",
    "leap":"leapt",
    "learn":"learnt",
    "leave":"left",
    "lend":"lent",
    "let":"let",
    "lie":"lay",
    "light":"lit",
    "lose":"lost",
    "make":"made",
    "mean":"meant",
    "meet":"met",
    "mow":"mowed",
    "pay":"paid",
    "put":"put",
    "read":"read",
    "ride":"rode",
    "ring":"rang",
    "rise":"rose",
    "run":"ran",
    "saw":"sawed",
    "say":"said",
    "see":"saw",
    "seek":"sought",
    "sell":"sold",
    "send":"sent",
    "set":"set",
    "sew":"sewed",
    "shake":"shook",
    "shine":"shone",
    "shoot":"shot",
    "show":"showed",
    "shrink":"shrank",
    "shut":"shut",
    "sing":"sang",
    "sink":"sank",
    "sit":"sat",
    "sleep":"slept",
    "slide":"slid",
    "smell":"smelt",
    "speak":"spoke",
    "speed":"sped",
    "spell":"spelt",
    "spend":"spent",
    "spit":"spat",
    "split":"split",
    "spoil":"spoilt",
    "spread":"spread",
    "spring":"sprang",
    "stand":"stood",
    "steal":"stole",
    "stick":"stuck",
    "sting":"stung",
    "stink":"stank",
    "stride":"strode",
    "strike":"struck",
    "swear":"swore",
    "sweep":"swept",
    "swim":"swam",
    "take":"took",
    "teach":"taught",
    "tear":"tore",
    "tell":"told",
    "think":"thought",
    "throw":"threw",
    "understand":"understood",
    "upset":"upset",
    "wake":"woke",
    "wear":"wore",
    "weep":"wept",
    "win":"won",
    "write":"wrote"}.items())
PHRASE = tuple({"works / you / where / Do / Danny / know / ? ":"Do you know where Danny works ?",
                "on / am / computer / I / my / playing":"I am playing on my computer",
                "London / but / do / No, / think / not / she / in / works / I / .":"No, but I do not think she works in London."}.items())
Nombre = tuple({"1":"one",
                "2":"two",
                "3":"three",
                "4":"four",
                "5":"five",
                "6":"six",
                "7":"seven",
                "8":"eight",
                "9":"nine",
                "10":"ten",
                "11":"eleven",
                "12":"twelve",
                "13":"thirteen",
                "14":"fourteen",
                "15":"fifteen",
                "16":"sixteen",
                "17":"seventeen",
                "18":"eighteen",
                "19":"nineteen",
                "20":"twenty",
                "21":"twenty one",
                "22":"twenty two",
                "23":"twenty three",
                "24":"twenty four",
                "25":"twenty five",
                "26":"twenty six",
                "27":"twenty seven",
                "28":"twenty eight",
                "29":"twenty nine",
                "30":"thirty",
                "31":"thirty one",
                "32":"thirty two",
                "33":"thirty three",
                "34":"thirty four",
                "35":"thirty five",
                "36":"thirty six",
                "37":"thirty seven",
                "38":"thirty eight",
                "39":"thirty nine",
                "40":"forty",
                "41":"forty one",
                "42":"forty two",
                "43":"forty three",
                "44":"forty four",
                "45":"forty five",
                "46":"forty six",
                "47":"forty seven",
                "48":"forty eight",
                "49":"forty nine",
                "50":"fifty"}.items())
WORD6 = tuple({"expérimentation animal":"animal testing",
               "each":"chaque, chacun",
               "colère":"anger",
               "disponible":"available",
               "match à l'extérieur":"away game",
               "quelqu'un":"anybody",
               "peu importe qui":"anyone",
               "récit, compte rendu":"account",
               "quotidien":"daily",
               "humide":"damp",
               "profond":"deep",
               "retarder,tarder":"delay",
               "profondeur":"depth",
               "noix de coco":"coconut",
               "couverture":"cover",
               "cuisinier":"cook",
               "elderly":"âgé",
               "disparu":"extinct",
               "conducteur, chauffeur":"driver",
               "tambour":"drum",
               "batterie":"drums",
               "vide":"empty",
               "fée":"fairy",
               "réfrigérateur":"fridge",
               "amusant, drôle":"funny",
               "furieux":"furious",
               "sentiment":"feeling",
               "premier plan":"foreground",
               "féroce":"ferocious",
               "en avant":"forward",
               "fondateur":"founder",
               "casier":"locker",
               "mot-clé":"keywords",
               "chevalier":"knight",
               "en direct":"live",
               "manque":"lack",
               "boîte aux lettres":"mailbox",
               "oncle":"uncle",
               "orage":"rainstorm",
               "oreille":"ear",
               "peu importe":"never mind",
               "patinoire":"rink",
               "ouverture":"opening",
               "partout":"everywhere",
               "piège":"trap",
               "pharse":"sentence",
               "patiner sur glace":"ice skate",
               "patron":"boss",
               "peindre":"painter",
               "plage":"beace",
               "drawing":"dessin",
               "to dream":"rêver"}.items())
CLOTHES = tuple ({"s'habiller":"to dress",
                "porter un vêtement":"to wear",
                "se déshabiller":"to undress",
                "enlever, ôter":"to take off",
                "élégant, chic":"elegant, smart",
                "les sous-vêtements":"underclothing, underwear",
                "un slip":"thunks, briefs",
                "une chemise": "a shirt",
                "un col":"a collar",
                "une cravate":"a tie",
                "un pantalon":"(a pair of) trousers",
                "une ceinture":"a belt",
                "une veste en cuir":"a leather jacket",
                "un manteau":"a coat",
                "une écharpe":"a scarf",
                "un imperméable":"a raincoat",
                "des pantoufles":"slippers",
                "un pull":"a jumper",
                "une robe":"a dress",
                "un sac à main":"a handbag",
                "la mode":"fashion",
                "des bijoux":"jewels",
                "une aiguille":"a needle",
                "des ciseaux":"scissors",
                "tricoter":"to knit",
                "":""}.items())
SPORTS = tuple ({"être passionné de football":"to be keen on football",
                "une équipe":"a team",
                "les joueurs":"the players",
                "le terrain":"the ground",
                "l'arbitre":"the referee",
                "le but":"the goal",
                "le gardien de but":"the goalkeeper",
                "marquer":"to score",
                "un match nul":"a draw",
                "s'entraîner":"to practise",
                "l'entraîneur":"the coach",
                "un court de tennis":"a tennis court",
                "la raquette":"the racket",
                "le filet":"the net",
                "un tournois":"a tournament",
                "l'athlétisme":"athletics",
                "une course":"a race",
                "la piste":"the track",
                "la boxe":"boxing",
                "la lutte":"wrestling",
                "le tir à l'arc":"archery",
                "l'escrime":"fencing",
                "une patinoire":"a skating rink",
                "l'escalade":"rock-climbing",
                "faire du ski":"to ski",
                "un remonte-pente":"a ski-lift",
                "l'équitation":"horse-rising",
                "un coucours hippipe":"a horse show",
                "un sportif":"a sportsman",
                "un aviron":"an oar",
                "plonger":"to dive",
                "nager":"to swim",
                "":""}.items())
Nourriture = tuple ({"pomme":"apple",
                "tarte aux pommes":"apple pie",
                "apprenti":"apprentice",
                "bacon":"bacon",
                "cuire (au four)":"bake",
                "banane":"banana",
                "haricot":"bean",
                "boeuf":"beef",
                "bière":"beer",
                "pain":"bread",
                "petit déjeuner":"breakfast",
                "beurre":"butter",
                "gâteau":"cake",
                "carrote":"carot",
                "ragoût":"casserole",
                "céréales":"cereal",
                "fromage":"cheese",
                "chewing-gum":"chewing gum",
                "poulet":"chicken",
                "frites":"chips",
                "chocolat":"chocolate",
                "cidre":"cider",
                "café":"coffee",
                "coca":"coke",
                "féliciter":"congratulate",
                "biscuits":"cookies",
                "chips":"crisps",
                "crème anglaise":"custard",
                "laiterie":"dairy",
                "décongeler":"defrost",
                "délicieux":"delicious",
                "dessert":"dessert",
                "beignet":"doughnut",
                "manger":"eat",
                "oeuf":"egg",
                "poisson":"fish",
                "nourriture":"food",
                "congeler":"freeze",
                "frais":"fresh",
                "frites":"fries (US)",
                "fruit":"fruit",
                "faire frire":"fry",
                "pamplemousse":"grapefruit",
                "jambon":"ham",
                "hamburger":"hamburger",
                "miel":"honey",
                "glace":"ice cream",
                "confiture":"jam",
                "gelée":"jelly",
                "ketchup":"ketchup",
                "":""}.items())
Nourriture2 = tuple ({"miel":"honey",
                "mouton":"mutton",
                "muffin":"muffin",
                "nourriture":"food",
                "orange":"orange",
                "organiser, préparer":"plan",
                "pâtes":"pasta",
                "petit pois":"peas",
                "pizza":"pizza",
                "poivre":"pepper",
                "pomme de terre":"potato",
                "porc":"pork",
                "préparer":"prepare",
                "pudding":"pudding",
                "recette":"recipe",
                "rôtir (faire)":"roast",
                "rouleau":"roll",
                "salade":"salad",
                "sandwitch":"sandwitch",
                "sauce":"sauce",
                "sauce à la menthe":"mint sauce",
                "scone":"scone",
                "sel":"salt",
                "servir":"serve",
                "steak":"steak",
                "sucre":"sugar",
                "tarte":"tart",
                "thé":"tea",
                "tomate":"tomato",
                "tourner la salade":"toss",
                "tourte":"pie",
                "tranche":"slice",
                "veau":"veal",
                "viande":"meat",
                "vin":"wine",
                "":""}.items())
soins = tuple ({"analgésique":"painkiller",
                "attraper":"catch",
                "avaler":"swallow",
                "aveugle":"blind",
                "bain":"bath",
                "chirurgien":"surgeon",
                "congé":"leave",
                "être couché":"lie",
                "dentiste":"dentist",
                "douche":"shower",
                "douleur":"pain",
                "douloureux":"painful",
                "enceinte":"pregnant",
                "éternuer":"sneeze",
                "examiner":"examine",
                "forme":"shape",
                "se fouler":"sprain",
                "grippe":"flu",
                "guérir":"recover",
                "handicapé":"disabled",
                "infirmière":"nurse",
                "faire mal":"hurt",
                "mal à la gorge (avoir)":"sore throat (have a)",
                "malade":"ill, sick",
                "maladie":"disease, illness, sickness",
                "maquillage":"make up",
                "maquiller (se)":"make up",
                "médecin":"doctor",
                "médicament":"medecine",
                "mort (n)":"death",
                "mort (adj)":"dead",
                "se moucher":"blow one's nose",
                "parfum":"perfume",
                "peser":"weigh",
                "poids":"weight",
                "prendre du poids":"put on weight",
                "raser (se)":"shave",
                "rasoir":"razor",
                "rayon X":"X-ray",
                "régime":"diet",
                "rhume":"cold",
                "somnifère":"sleeping pill",
                "souffrir":"suffer",
                "sourd":"deaf",
                "teindre":"dye",
                "tousser":"cough",
                "vie":"life",
                "":""}.items())
class fen_test(): ###################  Fenetre de reponse aux questions
    def __init__(self, parent, titre="test",ask="000",voc1="",voc2="",dico=WORDS1,path=".stats"):
      self.root = parent
      self.path = path
      self.titre = titre
      self.ask = ask
      self.voc1 = voc1
      self.voc2 = voc2
      self.dico = dico
      self.controle=[voc1]
      self.compteur_index=0
      self.compteur = 1
      self.bon = 0
      self.mauvais = 0
      self.root.title(self.titre)
      self.root.configure(bg="#eae596")
      self.root.resizable(width=False, height=False)
      if self.dico == PHRASE:
          self.root.geometry("450x250+400+100")
      else:
          self.root.geometry("250x250+400+100")
      Label(self.root,text = self.ask,bg="#eae596").pack()
      self.zero = StringVar()
      self.lb = StringVar()
      self.lb.set (self.voc1)
      Label(self.root,textvariable=self.lb, font="bold",bg="#eae596").pack()
      self.entree = Entry(self.root,textvariable = self.zero,width =30,fg="#010102",bg="white")
      self.entree.pack() # attention a bien separer la ligne grid dans un entry pour renvoyer la chaine
      Label(self.root,bg="#eae596").pack()
      btn = Button(self.root, text="Valider",command=self.evaluer).pack()
      Label(self.root,bg="#eae596").pack()
      #self.btn1 = Button(self.root, text="Info Session",command=self.pourcentage)
      #self.btn1.pack()
      Label(self.root,bg="#eae596").pack()
      btn = Button(self.root, text="Retour au menu",command=self.quitter).pack()
      Label(self.root,bg="#eae596").pack()

      self.aff_bon = StringVar()
      self.aff_bon.set(self.bon)
      Label(self.root, text="Réponse juste",bg="#eae596").pack()
      Label(self.root,textvariable=self.aff_bon,bg="#eae596").pack()
      self.root.mainloop()

    def quitter(self):
      r=open(self.path,"w")
      r.write("")
      r.close()
      b=open("/home/" + user + "/word.tmp", "w")
      b.write("")
      b.close()
      for index in range(len(self.controle)):
          print(index ,self.controle[index])
      self.root.destroy()
      main()
    def evaluer(self):



        if self.entree.get().strip() == self.voc2:
            self.entree.configure(bg='green')
            self.bon += 1
            self.compteur_index += 1
            self.compteur += 1

        else:
            self.entree.configure(bg='red')
            self.mauvais += 1
            self.compteur_index += 1
            self.compteur += 1
            if self.dico != PHRASE:
                showinfo('Résultat', 'La bonne réponse est: \n\n' + self.voc2)
            else:
                showerror("Message","Réfléchit un peu !")

        self.voc1, self.voc2 = self.dico[self.compteur_index]


        self.lb.set (self.voc1)
        self.voc2 = self.voc2
        self.aff_bon.set(self.bon)
        self.entree.configure(bg='white')
        self.zero.set("")
        self.entree.focus_set()

        if self.compteur == len(self.dico):
            self.pourcentage()
            self.root.update()







   
    def pourcentage(self): # Fonction de calcul du pourcentage de réussite
         somme = self.bon +self.mauvais
         pourcent = self.bon * 100 / somme
         conv = str(pourcent)
         mess = conv[:5] + " % de réussite\n"
         showinfo('Résultat', mess)
         log1  = self.path + "_"
         print (log1)
         r = open(log1,"a")
         date=datetime.now()
         date_day=date.day
         date_month=date.month
         date_year=date.year
         date_hour=date.hour
         date_minute=date.minute
         date_second=date.second
         r.write(str(date_day)+"/"+str(date_month)+"/"+str(date.year)+"---" + str(date_hour)+":"+str(date_minute)+":"+str(date_second)+"   ")
         r.write(self.titre + " " + mess)
         r.close()
         self.quitter()


class lecons():

    def __init__(self,parent):
        self.root = parent
        self.root.title("Fenetre des leçons")
        self.root.geometry("750x600+200+100")
        self.txt = StringVar()
        self.menubar = Menu(self.root)

        menu1 = Menu(self.menubar, tearoff=0)
        menu1.add_command(label="Le présent simple",command=self.lire_present_simple)
        menu1.add_command(label="Editer")
        menu1.add_separator()
        menu1.add_command(label="Quitter",command=self.quitter)
        self.menubar.add_cascade(label="Leçons", menu=menu1)
        self.root.config(menu=self.menubar)
        Label(self.root,textvariable = self.txt,justify = LEFT).grid(row=1, sticky=S)
        self.root.mainloop()
    def quitter(self):
        self.root.destroy()
        main()
    def lire_present_simple(self):

        file = open("/home/"+ user +"/.anglais_py/l_ps.txt","r")
        li = file.read()

        self.txt.set(li)

        file.close()

def main():
    def Vocabulaire_Anglais():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = WORDS1[0] # Choisi aléatoirement un tuple
        f = fen_test(root,"Les couleurs,jours,mois", "Quel est la traduction de:",word_to_translate,translated_word,WORDS1,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def verbe_irr():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = VERBE_IRR[0] # Choisi aléatoirement un tuple
        f = fen_test(root,"Verbe irréguliers", "Quel est la traduction de:",word_to_translate,translated_word,VERBE_IRR,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def verbe_irr_pret():
        fen_menu.destroy()
        root= Tk()
        word_to_translate, translated_word = random.choice(VERBE_IRR_PRET) # Choisi aléatoirement un tuple
        f = fen_test(root,"Conjuguer au prétérit", "Quel est le prétérit de:",word_to_translate,translated_word,VERBE_IRR_PRET,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def voc_2():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = random.choice(WORDS2) # Choisi aléatoirement un tuple
        f = fen_test(root,"Vocabulaire série n°2","Quel est la traduction de:",word_to_translate,translated_word,WORDS2,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def voc_3():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = WORDS3[0] # Choisi aléatoirement un tuple
        f = fen_test(root,"Les sentiments","Quel est la traduction de:",word_to_translate,translated_word,WORDS3,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def voc_4():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = Nourriture[0] # Choisi aléatoirement un tuple
        f = fen_test(root,"La nourriture","Quel est la traduction de:",word_to_translate,translated_word,Nourriture,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def voc_5():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = random.choice(WORDS5) # Choisi aléatoirement un tuple
        f = fen_test(root,"Vocabulaire série n°5","Quel est la traduction de:",word_to_translate,translated_word,WORDS5,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def Nour2():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = Nourriture2[0]
        f = fen_test(root,"Nourriture suite","Quel est la traduction de:",word_to_translate,translated_word,Nourriture2,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def fonc_soins():
        fen_menu.destroy()
        root = Tk()
        world_to_translate, translated_word = soins[0]
        f = fen_test(root,"Les soins du corps, la santé","Quel est la traduction de:",world_to_translate,translated_word,soins,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def voc_6():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = random.choice(WORD6)
        f= fen_test(root,"Vocabulaire série n°6","Quel est la traduction de:",word_to_translate,translated_word,WORD6,"/home/" + user + "/.stats")
    def lec():
        fen_menu.destroy()
        root = Tk()
        C = lecons(root)

    def remettre():
        fen_menu.destroy()
        root = Tk()
        word_to_translate, translated_word = random.choice(PHRASE)  # Choisi aléatoirement un tuple
        f = fen_test(root, "Remettre dans l'ordre", "Quel est la traduction de:", word_to_translate, translated_word,
                     PHRASE, "/home/"+ +"/.stats")
        root.mainloop()
        exit(0)
    def compter():
        fen_menu.destroy()
        root = Tk()
        nombre, translated_nombre= Nombre[0] # Choisi aléatoirement un tuple
        f = fen_test(root,"Compter","Quel est la traduction de:",nombre,translated_nombre,Nombre,"/home/" + user + "/.stats")
        root.mainloop()
        exit(0)
    def info():
       fen_menu.destroy()
    def quitter():
          root.destroy()
          main()
    def dernier():
        liste.delete(0,END)
        f = open("/home/" + user + "/.stats_","r")
        li=f.readlines() #Attention lit et sépare chaque ligne par un repèreset renvoie le résultat sous forme de liste

        f.close()#
        last_line = li [ len ( li ) -1] #Lit le dernier élément de la liste
        liste.insert(END, last_line)
        root = Tk()
        root.title('Informations')
        root.geometry("450x500+200+200")
        root.resizable(width=False,height=False)
        root.configure(bg="#9ED963")
        liste = Listbox(root,height=24,width=50)
        liste.pack(side=TOP)
        fd = open("/home/" + user + "/.stats_","r")
        li=fd.readline() # lit la premiere ligne
        i=1
        while li!='':
          liste.insert(i,li)
          li=fd.readline()
          i+=1
        fd.close()
    def tous():
          liste.delete(0,END)
          fd = open("/home/" + user + "/.stats_","r")
          li=fd.readline() # lit la premiere ligne

          i=1
          while li!='':
             liste.insert(i,li)
             li=fd.readline()
             i+=1
          fd.close()

          Button(root,text = "Retour au menu",command=quitter).pack(side=BOTTOM,pady=15)
          Button(root,text = "Dernière Session",command=dernier).pack(side=LEFT,padx=20)
          Button(root,text = "Toutes les Sessions",command=tous).pack(side=RIGHT,padx=20)
          root.mainloop()
    fen_menu = Tk()
    fen_menu.resizable(width=False, height=False)
    fen_menu.geometry("600x450+100+100")
    fen_menu.title('Logiciel de révision anglais --- Menu Principal')
    Button(fen_menu, text='Les couleurs, Les jours, Les mois, Les saisons',bg="yellow",command=Vocabulaire_Anglais).grid(row = 1, columnspan=2, pady=10)
    Button(fen_menu, text='Les sentiments',bg="yellow",command=voc_3).grid(row =2,padx=10,pady=10)
    Button(fen_menu, text='La nourriture',bg="yellow",command=voc_4).grid(row =2 , column =1,padx=10,pady=10)
    Button(fen_menu, text='La nourriture 2',bg="yellow",command=Nour2).grid(row =2 , column =2,padx=10,pady=10)
    Button(fen_menu, text='Vocabulaire série n°5', bg="yellow", command=voc_5).grid(row=3, column=1, padx=10, pady=10)
    Button(fen_menu,text='Vocabulaire série n°6', bg="yellow", command=voc_6).grid(row=3, padx=10,pady=10)

    Button(fen_menu,text='Les soins du corps, la santé', bg="yellow", command=fonc_soins).grid(row=3,column=2, padx=10,pady=10)
    Button(fen_menu, text='Verbes Irréguliers',bg="#3636b1",command=verbe_irr).grid(row =4,columnspan=2,pady=10)
    Button(fen_menu, text='Verbes Irréguliers Prétérit',bg="#3636b1",command=verbe_irr_pret).grid(row =5,columnspan=2,pady=10)
    Button(fen_menu, text="Remettre dans l'ordre",command=remettre).grid(row =6 ,columnspan=2,pady=10)
    Button(fen_menu, text="Compter",command=compter).grid(row=7, columnspan=2, pady=10)
    Button(fen_menu, text='Informations des sessions',bg="#3636b1",command=info).grid(row=8 ,columnspan=2, sticky=S,pady=10)
    Button(fen_menu, text='Quitter',command=sys.exit).grid(row=9, columnspan=2, pady=10)
    r=open("/home/"+ user +"/.stats","w")
    r.write("")
    r.close()
    b=open("/home/" + user + "/word.tmp", "w")
    b.write("")
    b.close()

    fen_menu.mainloop()
    exit(0)


if __name__ == "__main__":
    main()
