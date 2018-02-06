####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'DillyDilly' # Only 10 chars displayed.
strategy_name = 'Savagery'
strategy_description = 'Collude until Betrayed, do not trust those who have betrayed recently.'
 

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: # It's the first round; collude.
            return 'c'
    else: 
        if 'b' in their_history[-1:]:
            return 'b'
        else:
            if 'b' in their_history[-3:]: # If the other player has betrayed within last 3 rounds, 
                if random.random()<0.8: # 80% of the other rounds
                    return 'b'   
                else:
                    return 'c' 
            else:    
                    return 'c'         