# The example function below keeps track of the opponent's history and plays whatever the opponent played
#two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

count=0
quincy_count =0
prev_player =""
current_bot = ""
player_history = []
guess =""
play_order ={}

solv = {
"R": "P",
"P": "S",
"S": "R"
    }


def quincy_deal(index):
       guesses = ["P", "S", "S", "R", "P"]
       return guesses[(index-1) % len(guesses)]


def kris_deal():
    return solv[solv[prev_player]]



def abbey_deal():
    pass
def mrugesh_deal():
    pass


def player(prev_play, opponent_history=[]):
    global count, quincy_count , solv , prev_player ,current_bot ,play_order
    
    quincy_choices = ["R", "R", "P", "P", "S"]
    count+=1

    if prev_play != "":

        opponent_history.append(prev_play)
        if quincy_choices[(count-1) % len(quincy_choices)] == prev_play:
            quincy_count += 1
        else:
            quincy_count = 0

        if quincy_count >= 8 :
            guess= quincy_deal(count)
            player_history.append(guess)
            prev_player = guess
            return guess

    
    if len(opponent_history) == 0:
            guess = random.choice(["R", "P", "S"])
            player_history.append(guess)
            prev_player = guess
            return guess


    if len(player_history) >= 2:
            is_kris = True

            for i in range(1, min(15,len(player_history))):

                if opponent_history[-i] != solv[player_history[-i-1]]:
                    is_kris = False
                    break
    
            if is_kris:
                guess = kris_deal()
                player_history.append(guess)
                prev_player = guess
                return guess

            
    if len(player_history) >= 2:
            key = "".join(player_history[-2:])
            if key not in play_order:
                play_order[key] = {"R":0,"P":0,"S":0}
    
            if len(player_history) >= 3:
                prev_key = "".join(player_history[-3:-1])
                if prev_key not in play_order:
                    play_order[prev_key] = {"R":0,"P":0,"S":0}
                play_order[prev_key][player_history[-1]] += 1
    
            if key in play_order:
                prediction = max(play_order[key], key=play_order[key].get)
                guess = solv[solv[prediction]]
                player_history.append(guess)
                prev_player=guess
                return guess

    if len(opponent_history) >= 10:
            last10 = opponent_history[-10:]
            prediction = max(set(last10), key=last10.count)
            guess = solv[prediction]
            player_history.append(guess)
            prev_player=guess
            return guess

    guess = random.choice(["R","P","S"])
    player_history.append(guess)
    prev_player=guess
    return guess
