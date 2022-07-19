import time
import random
import os
from termcolor import colored
from replit import audio
fin = False
start = False
art1 = False
roverparts = False
redrocks = False
done69 = False
q1 = ""
source = audio.play_file('sample.wav')
while fin == False:
    qg = 0
    qn = " "
    uq2 = " "
    sq2 = " "
    done = False
    done2 = False
    one = False
    two = False
    correct = False
    rp = False
    rr = False
    fuel = 100
    shields = 100
    fire = ""
    ehp = 1
    crit = False
    hard = 1
    unobtainium = 0
    timer = 0
    spaceshipch = " "
    sputnik = 4
    torpedosx = ""
    torpedos = 10
    sputnikx = ""

    def end():
        global qg
        global correct
        global p1
        if qg == 1 and q == "hydrogen":
            correct = True
        if qg == 2 and q == "saturn":
            correct = True
        if qg == 3 and q == "jupiter":
            correct = True
        if qg == 4 and q == "venus":
            correct = True
        if qg == 5 and q == "earth":
            correct = True
        if qg == 6 and q == "mars":
            correct = True
        if qg == 7 and q == "earth":
            correct = True
        if qg == 8 and q == "venus":
            correct = True
        if qg == 9 and q == "mercury":
            correct = True
        if qg == 10 and q == "uranus":
            correct = True
        if qg == 11 and q == "pluto":
            correct = True
        if qg == 12 and q == "kuiper":
            correct = True
        if p1 == "hack":
            correct = True
        if (qg == 13 and q == "eris") or (qg == 13 and q == "ceres") or (
                qg == 13 and q == "haumea") or (qg == 13 and q == "makemake"):
            correct = True
        if qg == 14 and q == "b":
            correct = True
        if qg == 15 and q == "b":
            correct = True
        if (qg == 16 and q == "challenger") or (qg == 16 and q == "columbia"):
            correct = True
        if qg == 17 and q == "orion":
            correct = True
        if qg == 18 and q == "discovery":
            correct = True
        if qg == 19 and q == "7":
            correct = True

    def queston():
        global qg
        global qn
        global correct
        qg = random.randint(1, 17)
        if qg == 1:
            qn = "What is the main gas found on uranus"
        if qg == 2:
            qn = "What planet is “the jewel of the solar system”"
        if qg == 3:
            qn = "what planet has a big red spot"
        if qg == 4:
            qn = "Is named after a roman goddess of love"
        if qg == 5:
            qn = "What object in the solar system is known to have surface liquid?"
        if qg == 6:
            qn = "what is the red planet"
        if qg == 7:
            qn = "From the sun to what planet is a AU"
        if qg == 8:
            qn = "What is the hottest planet orbiting the solar system?"
        if qg == 9:
            qn = "What planets day is ⅔ of its year"
        if qg == 10:
            qn = "Only planet to rotate on its side"
        if qg == 11:
            qn = "was a planet until 2006"
        if qg == 12:
            qn = "Name the asteroid belt that Pluto is in"
        if qg == 13:
            qn = "Name one dwarf planet other than Pluto"
        if qg == 14:
            qn = "Does the sun do fission(A) or fusion?(B)"
        if qg == 15:
            qn = "Are there stronger tides during the quarters(A) or full/new(B) moon?"
        if qg == 16:
            qn = "name one of the catastrophic space shuttle missions"
        if qg == 17:
            qn = "what NASA spaceship is planned to go to mars"
        if qg == 18:
            qn = "What is the space shuttle held at the udvar hazy center"
        if qg == 19:
            qn = "How many rings does saturn have"

    def questoning():
        global correct
        global q
        global sn
        global fuel
        correct = False
        while correct == False:
            os.system("clear")
            print("To proceed you need to answer a planet question")
            queston()
            time.sleep(1)
            print("your queston is  '" + qn + "'")
            q = input(" ")
            end()
            time.sleep(1)
            if correct == False:
                print("wrong")
                print("next question")
                time.sleep(1)
        print("correct!")
        if sn == "hack":
            fuel = 100

    def gameover():
        global shields
        global fuel
        while 1 == 1:
            os.system("clear")
            print("""      █▀▀▀ █▀▀█ █▀▄▀█ █▀▀   █▀▀█ ▀█░█▀ █▀▀ █▀▀█
      █░▀█ █▄▄█ █░▀░█ █▀▀   █░░█ ░█▄█░ █▀▀ █▄▄▀
      ▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀   ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀""")
            if fuel < 1:
                print(
                    "uh oh you ran out of fuel and got sucked into the nearest planet! LAND ON A PLANET TO GATHER FUEL AND TO EXPLORE MORE PLANETS RESTART THE FUEL!!!!!"
                )
            if shields < 1:
                print(
                    "uh oh your shields went down and the solar wind gave you and your crew radiation poisoning!"
                )
            time.sleep(20)

    def fight():
        global fire
        global ehp
        global shields
        global crit
        global hard
        global torpedos
        global torpedosx
        global sputnik
        global spaceship
        global spaceship2
        global spaceship3
        ehp = random.randint(50, 100)
        won = False
        done3 = False
        if sn != "hack":
            if unobtainium == 1:
                print("do you want to use unobtainium it regenerates shields")
                un = input("[Y/N]")
                if un == "y":
                    shields = 100
                print("shields regenerated")
            while done3 == False:
                if torpedos > 9:
                    torpedosx = str(torpedos) + "x"
                if torpedos < 10:
                    torpedosx = " " + str(torpedos) + "x"
                sputnikx = str(sputnik) + "x"
                damage = 0
                crit = random.randint(1, 5)
                if hard == 1:
                    eatack = random.randint(1, 40)
                if hard == 2:
                    eatack = random.randint(40, 70)
                os.system("clear")
                damage = 0
                fire = " "
                print("the enemies shields are at " + str(ehp) + "%")
                print(sn + " shields are at " + str(shields) + "%")
                print(" _______________________________________")
                print("| torpedos  |   lazers   |   sputnik   |")
                print("|    1      |     2      |      3      |")
                print("|   " + str(torpedosx) + "     |     ∞      |      " +
                      str(sputnikx) + "     |")
                print("| 30 damage |  20 damage |  45 damage  |")
                print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                fire = input("[1/2/3]")
                if int(fire) == 1:
                    if torpedos > 0:
                        if crit == 1:
                            damage = 30
                            print("critical hit!")
                        damage = damage + 30
                        torpedos = torpedos - 1
                if int(fire) == 2:
                    if crit == 1:
                        damage = 40
                        print("critical hit!")
                    damage = damage + 40
                if int(fire) == 3:
                    if sputnik > 0:
                        if crit == 1:
                            damage = 45
                            print("critical hit!")
                        damage = damage + 45
                        sputnik = sputnik - 1
                if int(fire) == 1:
                    if torpedos < 1:
                        print("your out")
                if int(fire) == 3:
                    if sputnik < 1:
                        print("your out")
                ehp = ehp - damage
                shields = shields - eatack
                if ehp < 1:
                    done3 = True
                if shields < 1:
                    done3 = True
                time.sleep(2)
            if shields < 1:
                gameover()

    def travel():
        global timer
        global spaceshipch
        global p1
        global comp
        os.system("clear")
        var90 = 1
        var91 = 14
        timer = 0
        if comp == "1":
            if spaceshipch == "1":
                spaceship = "                 "
                spaceship2 = "＜██USA█████]＜@##"
                spaceship3 = "                 "
            if spaceshipch == "2":
                spaceship = "▄▄USA▄▄    ▄▄@## "
                spaceship2 = "     \\    /      "
                spaceship3 = "     ██████      "
            if spaceshipch == "3":
                spaceship = "                   "
                spaceship2 = "         ▄▄USA█    "
                spaceship3 = "-==二██████████@## "
        if comp == "2":
            if spaceshipch == "1":
                spaceship = "                  "
                spaceship2 = "＜██USSR████]＜@## "
                spaceship3 = "                  "
            if spaceshipch == "2":
                spaceship = "▄▄USSR▄    ▄▄@##  "
                spaceship2 = "     \\    /      "
                spaceship3 = "     ██████       "
            if spaceshipch == "3":
                spaceship = "                  "
                spaceship2 = "         ▄USSR█   "
                spaceship3 = "-==二██████████@##"
        if comp == "3":
            if spaceshipch == "1":
                spaceship = "                  "
                spaceship2 = "＜██ESA█████]＜@## "
                spaceship3 = "                  "
            if spaceshipch == "2":
                spaceship = "▄▄ESA▄▄    ▄▄@##  "
                spaceship2 = "     \\    /      "
                spaceship3 = "     ██████       "
            if spaceshipch == "3":
                spaceship = "                  "
                spaceship2 = "         ▄▄ESA█   "
                spaceship3 = "-==二██████████@##"
        if comp == "4":
            if spaceshipch == "1":
                spaceship = "                  "
                spaceship2 = "＜████X████]＜@## "
                spaceship3 = "                  "
            if spaceshipch == "2":
                spaceship = " ▄▄X▄▄▄▄    ▄▄@## "
                spaceship2 = "     \\    /      "
                spaceship3 = "     ██████       "
            if spaceshipch == "3":
                spaceship = "                  "
                spaceship2 = "           ▄▄X█   "
                spaceship3 = "-==二██████████@##"
        if p1 != "hack":
            while timer < 15:
                space2 = "   " * var90
                space1 = "   " * var91
                print(")" + space1 + spaceship + space2 + "(")
                print(")" + space1 + spaceship2 + space2 + "(")
                print(")" + space1 + spaceship3 + space2 + "(")
                print("			TRAVELLING			")
                timer = timer + 1
                var90 = var90 + 1
                var91 = var91 - 1
                time.sleep(0.5)
                os.system("clear")

    os.system("clear")

    def homescreen():
        print("welcome to                                              " +
              colored("▄███", "green") + colored("███", "cyan") +
              colored("▄", "green"))
        print("█░░ █▀▀█ █▀▀ ▀▀█▀▀   ░▀░ █▀▀▄   █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀ " +
              colored(" █", "cyan") + colored("█▀▀█", "green") +
              colored("██", "cyan") + colored("▀▀█", "green"))
        print("█░░ █░░█ ▀▀█ ░░█░░   ▀█▀ █░░█   ▀▀█ █░░█ █▄▄█ █░░ █▀▀ " +
              colored(" █", "cyan") + colored("█▄", "green") +
              colored("█████", "cyan") + colored("▄█", "green"))
        print("▀▀▀ ▀▀▀▀ ▀▀▀ ░░▀░░   ▀▀▀ ▀░░▀   ▀▀▀ █▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀  " +
              colored(" ▀██", "green") + colored("██", "cyan") +
              colored("██▀", "green"))

    homescreen()

    if start == False:
        p1 = input("player what is your name:")
        sn = input("what is your ships name:")
        start = True
    if done69 == True:
        print("would you like to look at your achievements")
        ach = input("[Y/N]")
        if ach == "y":
            print("your achievements are:")
            if roverparts == True:
                print("scavenger - pick up rover parts on Mars")
            if redrocks == True:
                print("geologist- pick up rocks")
            if art1 == True:
                print("collector- find the artifact")
            if unobtainium == 1:
                print("defender - pick up unobtainium")
            if unobtainium == 1:
                print("defender-")
            if roverparts == False:
                print("scavenger -")
            if redrocks == False:
                print("geologist-")
            if art1 == False:
                print("collector-")
            stop = input("hit enter to exit")
        print("do you want to play again")
        donee = input("[Y/N]")
        if donee == "n":
            while 1 == 1:
                os.system("clear")
                print("""MMMMMMMMMMMMMMMMMMMMMWN0OKWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOooOXWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKo;cxKWMMMMMMMM
MMMMMMMMMMN0kxkOO00XNWMMMMNk:,:dKWMMMMMM
MMMMMMMMN0o;'''',;lOXNMMMMMW0c,,:kNMMMMM
MMMMMMNOl;''''',ckXWMMMMMMMMWKl,',oKWMMM
MMMWNOl,'''''''c0WMMMMMMMMMMMW0c'',lKWMM
MMW0l,'''''','',ckXWMMMMMMMMMMWO:'',lXMM
MMMXkc,'',cxkl,'',ck0XWMMMMMMMMNd,'';xNM
MMMMWXxcckXWMNOl,'',;ckXWMMMMMMWk;'''lXM
MMMMMMWNNWMMMMWNOl,''',cxXWMMMMWO;'''lKM
MMMMMMMMMMMMMMMMWNOl;,'',cxXWMMNd,'''oXM
MMMMMMMMMMMMMMMMMMMNKOl,'',cxKNk:''';kWM
MMMMMMMWWX0OkOXWMMMMMMNkc,'',:c;''';xNMM
MMMMMWNOl;,,',:ok0KXNNNX0o,''''''':kNMMM
MMMWKkl;'';ll;''',;::ccc:;,'''''',lKWMMM
MNOo:,',cxKNN0xl;,'''''''''',::,'',:xKWM
Ko,''',oKWMMMMMNKOxdddooodxk0XKkc,'',:xX
d,'',:xXMMMMMMMMMMMMMMWWMMMMMMMWXkc,'',x
Oc,;o0WMMMMMMMMMMMMMMMMMMMMMMMMMMWKl,,c0""")
                time.sleep(20)
    time.sleep(1)
    os.system("clear")
    homescreen()
    print("""what ship do you want?
__________________________________________""")
    print("|  ⋀    |             |                 |")
    print("|  █    |             |                 |")
    print("|  █    | ▄▄   ▄▄▄▄▄▄▄| ██▄▄            |")
    print("|  █    |  \    //    | █████████二==-- |")
    print("|  █    |   █████     |                 |")
    print("|  ⋀    |             |                 |")
    print("|   1   |       2     |        3        |")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    spaceshipch = input("[1/2/3]")
    time.sleep(2)
    os.system("clear")
    homescreen()
    print("""what space company do you want?
	______________________________
	| NASA | USSR | ESA | SpaceX |
	|   1  |   2  |  3  |    4   |
	¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯""")
    comp = input("[1/2/3/4]")
    time.sleep(2)
    os.system("clear")
    print("welcome " + p1)
    print("You are on an adventure to get back to earth")
    print("You are currently on Neptune gathering gas to fuel your ship ")
    print("""facts:          	                                      	    """ +
          colored("▄██████▄", "blue"))
    print("	Mass:	102,410,000,000,000,000 billion kg (17.15x Earth)  " +
          colored("██████████", "blue"))
    print("	Equatorial Diameter:	49,528 km                          " +
          colored("██████████", "blue"))
    print("	Polar Diameter:	48,682 km                                   " +
          colored("▀██████▀", "blue"))
    print("""	Equatorial Circumference:	155,600 km
	Known Moons:	14
	Notable Moons:	Triton
	Known Rings:	5
	Orbit Distance:	4,498,396,441 km (30.10 AU)
	Orbit Period:	60,190.03 Earth days (164.79 Earth years)
	Surface Temperature:	-201 °C
	First Record:	September 23rd 1846
	Recorded By:	Urbain Jean Joseph Le Verrier & Johann Galle
	""")
    time.sleep(2)
    print("do you want to explore Neptune?")
    nq1 = input("[Y/N]")
    if nq1 == "y":
        os.system("clear")
        print(
            "Well here's the thing Neptune is a gas giant with no solid surface so. . ."
        )
        time.sleep(3)
        print("you cant land.")
        time.sleep(2)
        print("We will just guess that you want to go to the next planet now.")
    else:
        print("bypassing Neptune")
        time.sleep(1)

    questoning()
    fuel = fuel - 50
    if fuel < 1:
        gameover()
    print("you are now travelling to Uranus")
    time.sleep(2)
    travel()
    os.system("clear")

    print("you are now at Uranus")
    print(sn + "s fuel at " + str(fuel) + "% shields at " + str(shields) + "%")
    print("""facts:
	Mass:	86,810,300,000,000,000 billion kg (14.536 x Earth)  """ +
          colored("▄██████▄", "cyan"))
    print("	Equatorial Diameter:	51,118 km                    	   " +
          colored("██████████", "cyan"))
    print("	Polar Diameter:	49,946 km                                  " +
          colored("██████████", "cyan"))
    print("	Equatorial Circumference:	159,354 km                  " +
          colored("▀██████▀", "cyan"))
    print("""	Known Moons:	27
	Notable Moons:	Oberon, Titania, Miranda, Ariel & 	Umbriel
	Known Rings:	13
	Orbit Distance:	2,870,658,186 km (19.22 AU)
	Orbit Period:	30,687.15 Earth days (84.02 Earth years)
	Surface Temperature:	-197 °C
	First Record:	March 13th 1781
	Recorded By:	William Herschel""")
    print("do you want to explore Uranus?")
    print(colored("you need to refuel to get to the next planet!", "red"))
    print("hint: you can now explore")
    uq1 = input("[Y/N]")
    if uq1 == "y":
        while uq2 != "2":
            os.system("clear")
            if done == False and one == False:
                print("""1) do you want to gather fuel
        2) leave""")
            if done == True and one == False:
                print("""2) leave""")
            uq2 = input(" ")
            if uq2 == "1":
                if done == False:
                    print("gathering...")
                    time.sleep(3)
                    fuel = 100
                    print("fuel at 100%")
                    done = True
                    time.sleep(3)
    done = True
    if uq1 == "n":
        print("bypassing Uranus")
        time.sleep(1)

    questoning()
    fuel = fuel - 50
    if fuel < 1:
        gameover()
    done = False
    one = False
    print("you are now travelling to Saturn")
    time.sleep(2)
    travel()
    os.system("clear")

    print("you are now at Saturn")
    print(sn + "s fuel at " + str(fuel) + "% shields at " + str(shields) + "%")
    print("""facts:		                                                   """ +
          colored("  ▄██████▄", "yellow"))
    print("	Mass:	568,319,000,000,000,000 billion kg (95.16 x Earth)  " +
          colored("██████████", "yellow"))
    print("	Equatorial Diameter:	120,536 km                        " +
          colored("░░░░░░░░░░░░░░", "yellow"))
    print("	Polar Diameter:	108,728 km                                 " +
          colored("  ▀██████▀", "yellow"))
    print("""	Equatorial Circumference:	365,882 km
	Known Moons:	62
	Notable Moons:	Titan, Rhea & Enceladus
	Known Rings:	30+ (7 Groups)
	Orbit Distance:	1,426,666,422 km (9.58 AU)
	Orbit Period:	10,755.70 Earth days (29.45 Earth years)
	Surface Temperature:	-139 °C
	First Record:	8th Century BC
	Recorded By:	Assyrians""")
    print("do you want to explore Saturn?")
    sq1 = input("[Y/N]")
    if sq1 == "y":
        while sq2 != "2":
            os.system("clear")
            if done == False:
                print("""1) do you want to gather fuel
        2) leave""")
            if done == True:
                print("""2) leave""")
            sq2 = input(" ")
            if sq2 == "1":
                if done == False:
                    print("gathering...")
                    time.sleep(3)
                    fuel = 100
                    print("fuel at 100%")
                    done = True
                    time.sleep(1)
                    print("it seems that you picked up an artifact")
                    time.sleep(2)
                    art1 = True
        done = False
    if sq1 == "n":
        print("bypassing Saturn")
        time.sleep(1)

    questoning()
    fuel = fuel - 30
    if fuel < 1:
        gameover()
    done = False
    one = False
    print("you are now travelling to Jupiter")
    time.sleep(2)
    travel()
    os.system("clear")
    print("you are now at Jupiter")
    print(sn + "s fuel at " + str(fuel) + "% shields at " + str(shields) + "%")
    print(
        """facts:	  	                                                       """
        + colored("▄████████▄", "yellow"))
    print("	Mass:	1,898,130,000,000,000,000 billion kg (317.83 x Earth) " +
          colored("████████████", "yellow"))
    print("	Equatorial Diameter:	142,984 km                            " +
          colored("████████████", "yellow"))
    print("	Polar Diameter:	133,709 km                                    " +
          colored("████████████", "yellow"))
    print("	Equatorial Circumference:	439,264 km                     " +
          colored("▀████████▀", "yellow"))
    print("""	Known Moons:	67
	Notable Moons:	Io, Europa, Ganymede, & Callisto
	Known Rings:	4
	Orbit Distance:	778,340,821 km (5.20 AU)
	Orbit Period:	4,332.82 Earth days (11.86 Earth 	years)
	Surface Temperature:	-108°C
	First Record:	7th or 8th Century BC
	Recorded By:	Babylonian astronomers""")
    print("hint: there is something on jupiter")
    if fuel < 31:
        print(colored("you need to refuel to get to the next planet!", "red"))
    print("do you want to explore Jupiter?")
    jq1 = input("[Y/N]")
    jq2 = " "
    if jq1 == "y":
        while jq2 != "2":
            os.system("clear")
            if done == False and two == False:
                print("""1) do you want to gather fuel
        2) leave
        3) gather some unobtainium""")
            if done == True and two == False:
                print("""2) leave
        3) gather some unobtainium""")
            if done == False and two == True:
                print("""1) do you want to gather fuel
        2) leave""")
            if done == True and two == True:
                print("""2) leave""")
            jq2 = input(" ")
            if jq2 == "2":
                done = True
            if jq2 == "1":
                if done == False:
                    print("gathering...")
                    time.sleep(3)
                    fuel = 100
                    print("fuel at 100%")
                    done = True
                    time.sleep(3)
            if jq2 == "3":
                unobtainium = 1
                print("you have gathered some unobtainium")
                time.sleep(2)
                two = True
        done = False
        time.sleep(1)
    print("wait there is a pirate gang waiting outside Jupiter")
    print("you need to fight them to pass")
    time.sleep(2)
    print("loading wepons")
    fight()
    os.system("clear")
    print("congratulations you won!")
    time.sleep(1)
    print("proceeding to the asteroid belt")
    time.sleep(1)
    print("tip: pirates hide in the astroid belt")
    time.sleep(2)
    os.system("clear")
    fight()
    os.system("clear")
    print("good job!")
    print("uh oh more pirates")
    time.sleep(2)
    fight()
    os.system("clear")
    print("now going to Mars")
    time.sleep(1)
    print("but you still need to answer a planet question")
    time.sleep(1)

    questoning()
    fuel = fuel - 30
    if fuel < 1:
        gameover()
    done = False
    one = False
    print("you are now travelling to Mars")
    time.sleep(2)
    travel()
    os.system("clear")

    print("you are now at Mars")
    print(sn + "s fuel at " + str(fuel) + "% shields at " + str(shields) + "%")
    print("facts:	                                                        " +
          colored("▄██████▄", "red"))
    print("	Mass:	641,693,000,000,000 billion kg (0.107 x Earth) " +
          colored("██████████", "red"))
    print("	Equatorial Diameter:	6,805 km                       " +
          colored("██████████", "red"))
    print("	Polar Diameter:	6,755 km                                " +
          colored("▀██████▀", "red"))
    print("""	Equatorial Circumference:	21,297 km
	Known Moons:	2
	Notable Moons:	Phobos & Deimos
	Orbit Distance:	227,943,824 km (1.38 AU)
	Orbit Period:	686.98 Earth days (1.88 Earth years)
	Surface Temperature:	-87 to -5 °C
	First Record:	2nd Millenium BC
	Recorded By:	Egyptian astronomers""")
    print("do you want to explore Mars?")
    mq1 = input("[Y/N]")
    mq2 = ""
    mq3 = ""
    done = False
    donemars = False
    if mq1 == "y":
        done2 = False
        done = False
        mq2 = ""
        while mq2 != "2":
            os.system("clear")
            if done == False:
                print("""1) land
        2) leave""")
            if done == True:
                print("""2) leave""")
            mq2 = input(" ")
            if sq2 == "2":
                done = True
                time.sleep(2)
            if mq2 != "2":
                mq3 = ""
                done2 = False
                if donemars == False:
                    print("landing...")
                    time.sleep(3)
                    os.system("clear")
                    while done2 == False:
                        os.system("clear")
                        if rr == False and rp == False:
                            print("you can gather")
                            print("1) red rocks")
                            print("2) rover parts")
                            print("3) exit")
                        if rr == True and rp == False:
                            print("you can gather")
                            print("2) rover parts")
                            print("3) exit")
                        if rr == False and rp == True:
                            print("you can gather")
                            print("1) red rocks")
                            print("3) exit")
                        if rr == True and rp == True:
                            print("you can gather")
                            print("3) exit")
                        mq3 = input(" ")
                        if mq3 == "1":
                            rr = True
                            redrocks = True
                        if mq3 == "2":
                            roverparts = True
                            rp = True
                        if mq3 == "3":
                            done2 = True
                    donemars = True
                    time.sleep(3)
        done = False
    if sq1 == "n":
        print("bypassing Mars")
        time.sleep(1)

    questoning()
    fuel = fuel - 20
    if fuel < 1:
        gameover()
    print("you are now travelling to Earth")
    travel()
    time.sleep(2)
    os.system("clear")
    print("""facts:
	Mass:	5,972,190,000,000,000 billion kg
	Equatorial Diameter:	12,756 km
	Polar Diameter:	12,714 km
	Equatorial Circumference:	40,030 km
	Known Moons:	1
	Notable Moons:	The Moon
	Orbit Distance:	149,598,262 km (1 AU)
	Orbit Period:	365.26 Earth days
	Surface Temperature:	-88 to 58° C""")
    time.sleep(5)
    os.system("clear")
    print(
        """█▀▀ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █░░█ █░░ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀█ █▀▀▄ █▀▀
█░░ █░░█ █░░█ █░▀█ █▄▄▀ █▄▄█ ░░█░░ █░░█ █░░ █▄▄█ ░░█░░ ▀█▀ █░░█ █░░█ ▀▀█
▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀▀ ▀░▀▀ ▀░░▀ ░░▀░░ ░▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀""")
    print("you are back at earth!")
    print("achievements can be viewed at the home screen")
    donee = input("to be brought to the home screen hit enter")
    done69 = True
os.system("clear")
