 ------rock scissors paper game------


while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

    choice = int(input("player1 turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("player1 choice is: " + choice_name)
    print("\nplayer2 turn.......")

    player2_choice = random.randint(1, 3)
    if player2_choice == 1:
        player2_choice_name = 'Rock'
    elif player2_choice == 2:
        player2_choice_name = 'paper'
    else:
        player2_choice_name = 'scissor'

    print("player2 choice is: " + player2_choice_name)

    print(choice_name + " V/s " + player2_choice_name)

    if ((choice == 1 and player2_choice == 2) or
            (choice == 2 and player2_choice == 1)):
        print("paper wins")
        result = "paper"

    elif ((choice == 1 and player2_choice == 3) or
          (choice == 3 and player2_choice == 1)):
        print("Rock wins")
        result = "Rock"
    else:
        print("scissor wins")
        result = "scissor"

    if result == choice_name:
        print("<== player1 wins ==>")
    else:
        print("<== player2 wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")

