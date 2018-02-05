# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Brogrammers' # Only 10 chars displayed.
strategy_name = 'Adaptive Tit for Tat'
strategy_description = 'Start colluding and then repeat the opponent’s last choice for the rest of the round unless certain conditions are met'
   
def anticipate_betray(my_history, their_history):
    if len(my_history)>1 and their_history[-2] == 'b':
        return 'b'
    else:
        return 'c' 
                         
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.


    if len(my_history) == 0:
        return 'c'
    if len(my_history)>0:
        if their_history[-1] == 'c':
           return anticipate_betray(my_history, their_history)
        elif their_history[-1] == 'b':
            return 'b'
'''
   
    if len(my_history) == 0:
        return 'c'
    if len(my_history)>0:
        if their_history[-1] == 'c':
            if len(my_history)>1 and their_history[-2] == 'b':
                return 'b'
            else:
                return 'c' 
        elif their_history[-1] == 'b':
            return 'b'
'''           
