def RPS():
    
    #Gather players name
    print("Welcome to Rock Paper, Scissors")
    player1=input ("player 1, Enter your Name: ")
    player2= input("player 2, Enter your name: ")

    #Gather player moves
    p1_Choice=input(f"{player1}, choose your weapon Rock, Paper, Scissors")
    p2_Choice=input(f"{player2}, choose your weapon Rock, Paper, Scissors")

   #Compare player moves 

    if p1_Choice== "Rock" and p2_Choice == "paper":
        print(f"Rock beats scissors, {player1} WINS!")
    
    elif p1_Choice == "Paper" and p2_Choice == "Rock":
        print(F"paper beats rock, {player1} WINS!!")
    
    elif p1_Choice == "Scissors" and p2_Choice == "Paper":
         print(F"Scissors beats park, {player1} WINS!!")


    if p2_Choice== "Rock" and p1_Choice == "paper":
        print(f"Rock beats scissors, {player2} WINS!")
    
    elif p2_Choice == "Paper" and p1_Choice == "Rock":
        print(F"paper beats rock, {player2} WINS!!")
    
    elif p2_Choice == "Scissors" and p1_Choice == "Paper":
         print(F"Scissors beats park, {player2} WINS!!")

         if p1_Choice == p2_Choice:
             print("Wow You guys have the same mind!!! Its A DRAW!!")
         
        
    def IsValidMove(p1_choice):
        print("invalid move!! Try again!")
        
        if PlayerMove in ValidMoves:
            return True
        else:
            return False


RPS()