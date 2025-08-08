from colorama import init, Fore, Style
init(autoreset=True)

print(r"""
               ❤️💕💘 WELCOME TO THE LOVE CALCULATOR 💘💕❤️
""")


def calculate_letter_score(name_combined, letters):
    total = 0
    for letter in letters:
        count = name_combined.count(letter)
        time_word = "time" if count in [0, 1] else "times"
        print(Fore.CYAN + f"{letter.upper()} occurs {count} {time_word}")
        total += count
    return total

def generate_message(score):
    if score < 20:
        return Fore.RED + "💔 Umm... better luck in your next life?"
    elif score < 50:
        return Fore.YELLOW + "🤔 There's something, but it's complicated."
    elif score < 80:
        return Fore.GREEN + "💞 Sparks are flying!"
    else:
        return Fore.MAGENTA + "💖 Perfect match made in Python!"

def love_calculator():
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n💕 Welcome to the Python Love Calculator 💕")
    while True:
        name1 = input(Fore.LIGHTBLUE_EX + "Enter the first name: ").strip()
        name2 = input(Fore.LIGHTBLUE_EX + "Enter the second name: ").strip()

        if not name1 or not name2:
            print(Fore.RED + "Both names must be provided. Please try again.\n")
            continue

        combined_names = (name1 + name2).lower()
        print("\n🔎 Analyzing the names...\n")

        true_total = calculate_letter_score(combined_names, "true")
        print(Fore.YELLOW + f"Total TRUE score = {true_total}\n")

        love_total = calculate_letter_score(combined_names, "love")
        print(Fore.YELLOW + f"Total LOVE score = {love_total}\n")

        love_score = int(str(true_total) + str(love_total))
        print(Fore.LIGHTGREEN_EX + f"\n💘 Final Love Score = {love_score}")

        print(generate_message(love_score))

        replay = input(Fore.LIGHTBLUE_EX + "\nWant to try again? (yes/no): ").strip().lower()
        if replay != "yes":
            print(Fore.LIGHTWHITE_EX + "\nThanks for playing! ❤️\n")
            break

if __name__ == "__main__":
    love_calculator()
