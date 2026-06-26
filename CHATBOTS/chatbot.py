import re ,random
from colorama import Fore , init


init(autoreset=True)

destinations = {"beaches":["maldives", "bali","phuket"], "mountains":["himalayas", "swiss alps", "rocky mountains"], "cities":["new york", "tokyo","paris"]}

jokes = ["WHY DID THE COMPUTER GO TO THE DOCTOR ? .. BECAUSE IT HAD A VIRUS .","WHY DO PROGRAMS LIKE NATURE ?.. BECAUSE IT HAS A LOT OF BUGS ","WHY DO TRAVELLERS ALWAYS FEEL WARM ?.. BECAUSE THEY HAVE ALL THEIR HOT SPOTS"]

def normalise(text):
    return re.sub(r"\s+", " " text.strip().lower())

def recommend():
    print(Fore.CYAN + "TRAVEL BOT: BEACHES , MOUNTAINS OR CITIES ? ")
    preference = input(Fore.YELLOW +"You:")
    preference = normalise(preference)

    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(Fore.CYAN + f"TRAVEL BOT: HOW ABOUT{suggestions} ")
        print(Fore.BLUE +"DO YOU LIKE IT ? (YES/NO)")
        answer = input(Fore.YELLOW+"You: ").lower()

    if answer == "yes":
        print(Fore.GREEN +f"TRAVEL BOT: GREAT!! ENJOY YOU DESTINATON - {suggestions}")

    elif answer == "no":
        print(Fore.Red +"LETS TRY ANOTHER ONE ")
        recommend()

    else:
        print(Fore.RED +"NO PROBLEN I WILL SUGGEST ANOTHER ONE ")
        recommend()

def packing():
    print(Fore.CYAN + " WHERE TO ?")
    location = normalise(input(Fore.YELLOW + "You: ").lower)

    




