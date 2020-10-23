import random

print('Rock...')
print('Paper...')
print('Scissors...')
a = "y"
while a == "y":
    p1_wins = 0
    p2_wins = 0
    com_wins = 0
    win_score = int(input("define a wining score :"))
    gameMode = input("please choose a game mode (pvp or pvc)")
    if gameMode == "pvc":
        print(gameMode)
        while p1_wins < win_score and com_wins < win_score:
            print(f"Player_1 score : {p1_wins}    com score : {com_wins}")
            Player_1 = input('Player_1 , Make your move :').lower()
            com = random.choice(["rock", "scissor", "paper"])
            if Player_1 == "surrender" or Player_1 == "quit":
                print(f"Player_1 score : {p1_wins}    com : {com_wins}")
                print("Player_1 surrendered , com wins")
                break
            else:
                print(f"com chose {com}")
                if Player_1 == com:
                    print("Tie")
                elif Player_1 == "rock":
                    if com == "scissor":
                        print("Player_1 Wins")
                        p1_wins += 1
                    elif com == "paper":
                        print("com Wins")
                        com_wins += 1
                    else:
                        print("Something went wrong ...")
                elif Player_1 == "scissor":
                    if com == "paper":
                        print("Player_1 Wins")
                        p1_wins += 1
                    elif com == "rock":
                        print("com Wins")
                        com_wins += 1
                    else:
                        print("Something went wrong ...")
                elif Player_1 == "paper":
                    if com == "rock":
                        print("Player_1 Wins")
                        p1_wins += 1
                    elif com == "scissor":
                        print("com Wins")
                        com_wins += 1
                    else:
                        print("Something went wrong ...")
                else:
                    print("Something went wrong ...")
                if p1_wins == win_score or com_wins == win_score:
                    if p1_wins > com_wins:
                        print("Player_1 Wins the match !!!")
                    elif com_wins > p1_wins:
                        print("com Wins the match !!!")
                    elif com_wins == p1_wins:
                        print("the match ended with a Tie !!!")
        print(f"Player_1 score : {p1_wins}    com score : {com_wins}")
    elif gameMode == "pvp":
        print(gameMode)
        while p1_wins < win_score and p2_wins < win_score:
            print(f"Player_1 score : {p1_wins}    Player_2 score : {p2_wins}")
            Player_1 = input('Player_1 , Make your move :').lower()
            Player_2 = input('Player_2 , Make your move :').lower()
            if Player_1 == "surrender" or Player_2 == "surrender" or Player_1 == "quit" or Player_2 == "quit":
                print(f"Player_1 score : {p1_wins}    Player_2 score : {p2_wins}")
                if Player_1 == "surrender" or Player_1 == "quit":
                    print("Player_1 surrendered , Player_2 wins")
                    break
                elif Player_2 == "surrender" or Player_2 == "quit":
                    print("Player_2 surrendered , Player_1 wins")
                    break
            else:
                print(f"Player_2 chose {Player_2}")
                if Player_1 == Player_2:
                    print("Tie")
                elif Player_1 == "rock":
                    if Player_2 == "scissor":
                        print("Player_1 Wins")
                        p1_wins += 1
                    elif Player_2 == "paper":
                        print("Player_2 Wins")
                        p2_wins += 1
                    else:
                        print("Something went wrong ...")
                elif Player_1 == "scissor":
                    if Player_2 == "paper":
                        print("Player_1 Wins")
                        p1_wins += 1
                    elif Player_2 == "rock":
                        print("Player_2 Wins")
                        p2_wins += 1
                    else:
                        print("Something went wrong ...")
                elif Player_1 == "paper":
                    if Player_2 == "rock":
                        print("Player_1 Wins")
                        p1_wins += 1
                    elif Player_2 == "scissor":
                        print("Player_2 Wins")
                        p2_wins += 1
                    else:
                        print("Something went wrong ...")
                else:
                    print("Something went wrong ...")
                if p1_wins == win_score or p2_wins == win_score:
                    if p1_wins > p2_wins:
                        print("Player_1 Wins the match !!!")
                    elif p2_wins > p1_wins:
                        print("Player_2 Wins the match !!!")
                    elif p2_wins == p1_wins:
                        print("the match ended with a Tie !!!")
        print(f"Player_1 score : {p1_wins}    Player_2 score : {p2_wins}")
    else:
        print("something went wrong")

    a = input("Again ? (Y/N)").lower()
