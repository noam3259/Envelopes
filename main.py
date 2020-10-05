# This is a sample Python script.

# Comments

import random
from envelope import Envelope




from strategy import BaseStrategy, Automatic_BaseStrategy, N_max_strategy, More_then_N_percent_group_strategy

if __name__ == '__main__':



    def cls():
        print("\n" * 20)




    envelopes = []
    for i in range(100):
        money = random.randrange(1, 5000)
        envelopes.append(Envelope(money))
    '''
    
    '''
    strategies = []
    strategies.append(BaseStrategy(envelopes))

    strategies.append(Automatic_BaseStrategy(envelopes))



    strategies.append(N_max_strategy(envelopes))


    strategies.append(More_then_N_percent_group_strategy(envelopes, 0.25))


    n = -1
    while n != 4:
        cls()
        for i in range(len(strategies)):
            print(str(i), strategies[i].display())
        n = input(f'enter your choice [0-{len(strategies)}] (len(strategies) to end):')
        if n.isdigit():
            n = int(n)
            if n == 2:
                N = input(f'enter N max values: ')
                strategies[n].N = int(N)
            elif n == 3:
                p = input(f'enter 0-1 number for group size (defualt=0.25)')
                strategies[n].percent = p
            if n != 4:
                strategies[n].play()
            x = input('press any key to continue')
        else:
            pass




