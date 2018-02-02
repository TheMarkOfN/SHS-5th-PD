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
    
def move_2(my_history, their_history, my_score, their_score):
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
        if len(their_history) == 0:
            return('b')
        else:
            if len(their_history) < 10:
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
                
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    betrays = 0
    if not 'b' or 'c' in their_history:
        return('b')
    else:
        if len(their_history) == 0:
            return('c')
        else:
            if len(their_history) < 10:
                if 'b' == their_history[-1]:
                    if len(their_history) > 1:
                        if 'b' == their_history[-2]:
                            return('b')
                        else:
                            return('c')
                    else:
                        return('c')
                else:
                    return('b')
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
                
                    
def test_move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    betrays = 0
    if not 'b' or 'c' in their_history:
        return('b')
    else:
        if len(their_history) == 0:
            return('c')
        else:
            if len(their_history) < 10:
                if 'bbb' in their_history:
                    return('b')
                else:
                    if random.randint(1,10) > 2.5:
                        return('c')
                    else:
                        return('b')
            else:
                for i in their_history[-1:-20]:
                    if i is 'b': #if a syntax, then replace is with =
                        betrays = betrays + 1
                if betrays > 7.5:
                    if random.randint(1,10) < 18.5:
                        return('b')
                    else:
                        return('c')
                if betrays > 5.5 and betrays < 15.5:
                    if random.randint(1,10) < 7.5:
                        return('b')
                    else:
                        return('c')
                if betrays < 10.5:
                    if random.randint(1,10) > 4.5:
                        return('b')
                    else:
                        return('c')

def test_move_2(my_history, their_history, my_score, their_score):
    '''Alternative move number 2'''
    
    betrays = 0
    percent_betrayed = betrays/len(their_history)
    if len(their_history) == 0:
        return('b')
    else:
        for i in their_history:
            if i == 'b':
                betrays = betrays + 1
        if percent_betrayed <= .25:
            if random.randint(1,10) < 2.5:
                return('b')
            else:
                return('c')
        if percent_betrayed > .25 and percent_betrayed <= .5:
            if random.randint(1,10) < 4.5:
                return('b')
            else:
                return('c')
        if percent_betrayed >.5 and percent_betrayed <=  .75:
            if random.randint(1,10) > .45:
                return('b')
            else:
                return('b')
        if percent_betrayed > .75:
            if random.randint > .25:
                return('b')
            else:
                return('c')