import random

tries = 8
list_ = ['python', 'java', 'kotlin', 'javascript']
user_input = set()

random.seed()
choice = random.choice(list_)
temp_for_choice = list(len(choice) * "-")
separator = ""
still_playing = True

print("H A N G M A N\n")
decision = input("Type \"play\" to play the game, \"exit\" to quit:")
while decision == "play":
    while tries and still_playing:
        print(separator.join(temp_for_choice))
        letter = input("Input a letter: ")
        if len(letter) == 1:
            if letter.isascii() and letter.islower():
                if letter not in user_input:
                    if letter not in choice:
                        if tries == 1:
                            print("""No such letter in the word
You are hanged!""")
                            tries -= 1
                            still_playing = False
                            input()
                            break
                        else:
                            print("No such letter in the word\n")
                            tries -= 1
                            user_input.add(letter)

                    else:
                        for i in range(len(choice)):
                            if letter == choice[i]:
                                temp_for_choice[i] = letter
                                user_input.add(letter)
                                print()
                                if separator.join(temp_for_choice) == choice:
                                    print(separator.join(temp_for_choice))
                                    print("""You guessed the word {}!
You survived!""".format(choice))
                                    still_playing = False
                                    input()
                                    break
                                i += 1

                else:
                    print("You already typed this letter\n")

            else:
                print("It is not an ASCII lowercase letter\n")
        else:
            print("You should input a single letter\n")

    decision = input("Type \"play\" to play the game, \"exit\" to quit:")
    if decision == "play":
        still_playing = True
        random.seed()
        choice = random.choice(list_)
        temp_for_choice = list(len(choice) * "-")
        user_input = set()
        tries = 8
