from Player import Player

#Rock, Paper, Scissors - Win Strategy
# Player1 play values:
# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3
# Player2 outcomes:
# X = Lose
# Y = Draw
# Z = Win
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
    "A": 1, #rock
    "B": 2, #paper
    "C": 3, #scissors
}
playOutcome = {
    "X": 'L',
    "Y": 'D',
    "Z": 'W',
}

for r in rounds:
    strategyClue = r.split(' ')
    outcome = playOutcome[strategyClue[1]]
    p1Play = playPoints[strategyClue[0]]
    Player.addPoints(player1, p1Play)

    #if outcome D p2play=p1play and both +3
    if outcome == 'D':
        Player.addPoints(player1, 3)
        Player.addPoints(player2, 3)
        Player.addPoints(player2, p1Play)
    #if outcome L, give p1 6 points for winning
    elif outcome == 'L':
        Player.addPoints(player1, 6)
        #if p1 rock then p2 scissors
        if p1Play == 1:
            Player.addPoints(player2, 3)
        #if p1 paper then p2 rock
        elif p1Play == 2:
            Player.addPoints(player2, 1)
        #else p1 scissors and p2 paper
        else:
            Player.addPoints(player2, 2)
    #else give p2 6 points for winning
    else:
        Player.addPoints(player2, 6)
        #if p1 rock then p2 paper
        if p1Play == 1:
            Player.addPoints(player2, 2)
        #if p1 paper then p2 scissors
        elif p1Play == 2:
            Player.addPoints(player2, 3)
        #else p1 scissors and p2 rock
        else:
            Player.addPoints(player2, 1)
    
print("Player1 final score: " + str(Player.__getattribute__(player1, "points")))
print("Player2 final score: " + str(Player.__getattribute__(player2, "points")))

input()
