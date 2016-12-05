import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'team11' # Only 10 chars displayed.
strategy_name = 'modified tft'
strategy_description = 'How does this strategy decide?'
    
'modified tft'
strategy_description = 'modified tft.'
    
def move(my_history, their_history, my_score, their_score):
    move = ''
    '''modefied tit for tat strategy'''
    rounds = len(my_history)
    if rounds == 0:
        move = 'c'
    else:
        if their_history[-1] == 'b':
            if random.randint(1, 7) == 3:
                move = "c"
            else:
                move = 'b'
        elif their_history[-1] == 'c':
            move = 'c'
    return move
    

    
