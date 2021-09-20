from random import randint
from random import shuffle

num = input('Hello there ✋,How many are you?: \n')
print(num)
team_list = list(range(1,int(num)+1))
print(team_list)

print('Now that i know how many are you, eah one is going to enter a name and a number from the ones you gave me then i will let you know the performer')
print('Good Luck, Let\'s go')

# myRandom = randint(1,3)
# print(myRandom)

team_dict = {}
def gather_team_info(num,team_dict):
    count = 1
    while count <=int(num):
        name = input('Enter your  name: \n')
        number = input('Enter your favorite number: \n')
        team_dict[number] =name
        count = count+1
    else:
         return  team_dict
        


result =gather_team_info(num,team_dict)
print(result)

def shuffle_team (team):
    shuffle(team)

    return team
shuffled_team = shuffle_team(team_list)
print(f'ShuffledTeam: {shuffled_team}')

def pick_random(num):
    return randint(1,int(num))

random_num = pick_random(num)

print(f'random_num: {random_num}')

def find_performer():
    for p in shuffled_team:
        if p ==random_num:
            print(f' team:{p}')
        else:
            pass
        return p
        
performer = find_performer()

print(f'performer:{performer}')

def pick_name(n):
    for key,val in team_dict.items():
        if key==performer:
            print(f'item:{val}')
            print(f"key {key}")
        else:
            pass
pick_name(performer)




