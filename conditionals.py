# Changed locally.

user_input = input("Are you a cigarette addict older than 75 years old? [yes/no]")
age = user_input == "yes"

user_input = input("Do you have a severe chronic disease? [yes/no]")
chronic = user_input == "yes"

user_input = input("Is your immune system too weak? [yes/no]")
immune = (user_input == "yes")

risk = age and chronic and immune

if risk:
    print("You are in risky group")
else:
    print("You are not in risky group")

