####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


import random

team_name = 'Byte Me' # Only 10 chars displayed.
strategy_name = 'The Social Experiment'
strategy_description = 'Start with collude until betrayed, then goes to soft majority'
    
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
    
    betrays = 0
    if not 'b' or 'c' in their_history:
        return('b')
    else:
        if len(their_history)<10:
            if 'b' in their_history:
                return('b')
            else:
                return('c')
        else:
            for i in their_history[-1:-10]:
                if i is 'b': #if a syntax, then replace is with =
                    betrays = betrays + 1
            if betrays > 7.5:
                if random.randint(1,10) < 9.5:
                    return('b')
                else:
                    return('c')
            if betrays > 5.5 and betrays < 7.5:
                if random.randint(1,10) < 7.5:
                    return('b')
                else:
                    return('c')
            if betrays < 5.5:
                if random.randint(1,10) > 4.5:
                    return('b')
                else:
                    return('c')
                
