
   ----Rock paper scissor game using functions-----
 

def game(player1, player2):
    if player1 == player2:
       return("tie!\n are you wanna play again")

    elif player1 == 'rock':
        if player2 == 'scissors':
            return("player1 won\n congratualations ")
        else:
            return("playe2 won\n congrats")

    elif player1== 'scissors':
        if player2 == 'paper':
            return("player1 won\n congratualations ")
        else:
            return("playe2 won\n congrats ")

    elif player1 == 'paper':
        if player2 == 'rock':
            return("player1 won\n congratualations")
        else:
            return("player2 won\n congrats ")
while True:
     choice = input("do you wann paly game")
     if choice == 'yes':
        print(game(input("player1,Enter your choice: "), input("player2,Enter your choice: ")))
     else:
         print("Run again to play")
