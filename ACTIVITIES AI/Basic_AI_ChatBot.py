print("HELLO I AM YOUR ADVANCE AI SYSTEM")

name = input("MAY I KNOW YOUR NAME : ")

occupation = input("PLEASE TELL ME ABOUT YOUR OCCUPATION: ")



print(f"WOW! {name}, SO YOU ARE A {occupation}")

mood = input("HOWS YOUR MOOD TODAY ?: ").lower()

if mood == "good":
    print("GREAT!")

elif mood == "bad":
    print("SO SAD TO HEAR THAT")

else:
    print("INVALID")


family = int(input("HOW MANY MEMBERS ARE THERE IN YOUR FAMILY ? :"))

print(f"GOOD To HEAR THAT {name}, THAT YOU HAVE {family} MEMBERS")


