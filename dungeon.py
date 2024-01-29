import time, math, random


player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
getal1 = random.randint(10,25)
getal2 = random.randrange(-5,75)
oparator = random.choice(["+","-","*"])
rekensom = f"{getal1} {oparator} {getal2}"
uitkomst = eval(rekensom)

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {rekensom}=?')
print(uitkomst)
antwoord = int(input('Wat toest je in?'))

if antwoord == uitkomst:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    sleutel = 1
else:
    print('Er gebeurt niets....')
    sleutel = 0
print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)

# === [kamer 6] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        player_hp =  player_health - player_attack_amount * zombie_hit_damage 
        print(f'Je health is nu {player_hp}.')
        
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()                      
print('')
time.sleep(1)



# === [kamer 3] === #
item = random.choice(['schild',"zwaard"])
if item == "shild":
    player_defense += 1
else:
    player_attack +=2

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
vijand_attack = 2
vijand_defense = 0
vijand_health = 3

vijand_hit_damage = (vijand_attack - player_defense)
if vijand_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    vijand_attack_amount = math.ceil(player_health / vijand_hit_damage)
    
    player_hit_damage = (player_attack - vijand_defense)
    player_attack_amount = math.ceil(vijand_health / player_hit_damage)

    if player_attack_amount < vijand_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        player_hp =  player_health - player_attack_amount * vijand_hit_damage 
        print(f'Je health is nu {player_hp}.')
        
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel == 1:
    print("je opent de schatkist en vind waardevole munten en neemt ze mee")
    print("Gefeliciteerd je hebt gewonnen")
else:
    print('helaas heb je geen sleutel dus je kan de schatkist niet openen')
    print("Je hebt de schat niet gevonden probreer het opnieuw")