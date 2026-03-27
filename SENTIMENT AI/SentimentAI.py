import colorama 
from colorama import Fore , Style 
from textblob import TextBlob 


colorama.init()

print(f"\n{Fore.CYAN}HELLO AND WELCOME TO SENTIMENTAL AI 😎!!!!!{Style.RESET_ALL}")

user_name = input(f"\n{Fore.RED}PLEASE ENETR YOUR NAME : {Style.RESET_ALL}").strip()

if not user_name :
    print(f"OH I SEE !! you want to be Mysterious \n from now on lets call you Mr. Mysterio 😋😎")
    user_name = "Mr. Mysterio"


conversational_history = []

print(f"{Fore.YELLOW}HELLO AGENT {user_name}😎{Style.RESET_ALL}")
print(f"\nLETS TRY SOMETHING SHALL WE ? ")
print(f"\n Type something and i will tell you the polarity of the sentence🙌")
print(f"\n and Agent {user_name} if You want any help you can type 'info' in the chat😊✏️ ")

while True:
    user_input = input(f"\n{Fore.RED}>>>{Style.RESET_ALL}")

    if user_input.lower() ==  "info":
        print(f"{Fore.MAGENTA}YOU CAN USE DIFFERENT FUNCTIONS LIKE{Style.RESET_ALL}\n{Fore.YELLOW}1) History{Style.RESET_ALL}\n{Fore.YELLOW}2) Reset{Style.RESET_ALL}\n{Fore.YELLOW}3) Exit{Style.RESET_ALL}")

    elif user_input.lower() == "exit":
        print(f"{Fore.CYAN}ROGER THAT {user_name}GOOD THAT YOU GAVE ME A TRY !!🙏🏼{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversational_history.clear()
        print(f"{Fore.CYAN}ROGER THAT {user_name}WILL RESET ALL YOUR HISTORY{Style.RESET_ALL}") 


    elif user_input.lower() == "history":
        if not conversational_history:
            print(f"\n\n {Fore.YELLOW}OH I CAN SEE HERE THAT THERE IS NO CONCERSTAIONAL HISTORY HERE 😢{Style.RESET_ALL}")

        else:
            print(f"\n {Fore.MAGENTA} CONVERSATIONAL HISTORY :- {Style.RESET_ALL}")
            for idx, (text,polarity,sentiment) in enumerate (conversational_history, start=1):
                
                if sentiment == "Positive":
                    color = Fore.GREEN
                    emoji = "😍"

                if sentiment == "Negative":
                    color = Fore.RED
                    emoji = "😍"

                else:
                    color == Fore.YELLOW
                    emoji = "😒"
                print(f"{idx} . {color}{text}" f"\n{polarity:.2f} ,{sentiment} {Style.RESET_ALL}")
            continue



    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment= "Neutral"
        color = Fore.YELLOW
        emoji = "😭"


    conversational_history.append((user_input, polarity, sentiment))
    print(f"{color}.{emoji}{sentiment} SENTIMENT DETECTED"
          f"\nPOLARITY:- {polarity:.2}")











