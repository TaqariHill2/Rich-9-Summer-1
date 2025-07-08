import random

players= ["Jeffery", "Max?", "Braylen", "Ollie",
         "Xavier", "Avery", "Carl", "Walter", 
        "Darren", "EJ", "Nahum", "Joqaiun",
        "Marshawn", "Ja'den", "Isaiah", "Kenlon",
        "Nishad", "Kauri", "Kriss", "Joseph",
        "Semaj","Tay", "Taqari", "Jamauri"]

def PickTeams (players):
    random.shuffle (players)
    team1 = players[:len(players) //2]
    teamCaptin1 = team1[random.randrange(0, 13)]

    print("Team 1:")
    print("Team 1 Captain " + teamCaptin1)
    for player in team1:
        print(team1)
   
PickTeams(players)

team2 = players[len(players)//2:]
TeamCaptin(2):
print(" Team 2 captain: " + TeamCaptain2)