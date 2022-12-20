from Player import Player

#Rock, Paper, Scissors - Win Strategy
# A, X = Rock = 1
# B, Y = Paper = 2
# C, Z = Scissors = 3
# games = many rounds
# round won = 6
# round drawn = 3
# round lost = 0
# first letter in txt is opponents play, 2nd is yours

file_str = open('c:\\Users\\ruth_\\Documents\\Side Projects\\AdventOfCode\\AdventOfCode\\2022\\Day 2\\Input.txt','r').read()
rounds = file_str.split("\n")

player1 = Player()
player2 = Player()

playPoints = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

for r in rounds:
    plays = r.split(' ')
    #Gets points for play and adds to totals
    Player.__setattr__(player1, "lastPlayPoints", playPoints[plays[0]])
    Player.__setattr__(player2, "lastPlayPoints", playPoints[plays[1]])
    Player.addPoints(player1, playPoints[plays[0]])
    Player.addPoints(player2, playPoints[plays[1]])
    #if draw, both get 3 points
    if Player.__getattribute__(player1, "lastPlayPoints") == Player.__getattribute__(player2, "lastPlayPoints"):
        Player.addPoints(player1, 3)
        Player.addPoints(player2, 3)
    #if p1 plays rock
    elif Player.__getattribute__(player1, "lastPlayPoints") == 1:
        #if p2 plays paper, p2 wins and gets 6 points
        if Player.__getattribute__(player2, "lastPlayPoints") == 2:
            Player.addPoints(player2, 6)
        #else p2 plays scissors, p1 wins and gets 6 points
    #if p1 plays paper
    elif Player.__getattribute__(player1, "lastPlayPoints") == 2:
        #if p2 plays scissors, p2 wins and gets 6 points
        if Player.__getattribute__(player2, "lastPlayPoints") == 3:
            Player.addPoints(player2, 6)
        #else p2 plays rock, p1 wins and gets 6 points
    #else p1 plays scissor
    #if p2 plays rock, p2 wins and gets 6 points
    elif Player.__getattribute__(player2, "lastPlayPoints") == 1:
        Player.addPoints(player2, 6)
        #else p2 plays paper, p1 wins and gets 6 points
    else:
        Player.addPoints(player1, 6)

print("Player1 final score: " + str(Player.__getattribute__(player1, "points")))
print("Player2 final score: " + str(Player.__getattribute__(player2, "points")))

input()
