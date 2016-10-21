#!/usr/bin/env python
import os


def screen():
    clear = os.system('clear')
    a = '''
##############################################################################
##############################################################################
____ ____ ___  ____ ____ _  _ ____ ___
|__/ |__|   /  |  | |__/ |\ | |___  |
|  \ |  |  /__ |__| |  \ | \| |___  |

Razornet BBS Verson Alpha.01
Author: John Galbraith                 
##############################################################################
Q = Quit, E = Email, B = Boards, C = Chat, D = Documents, G = Games
\n'''
    return a




run = True
status = 'Welcome!\n'
invalid_count = 0

while run is True:
    print screen()
    print status
    option = str(raw_input('&> '))

    if option.lower() == 'q':
        run = False
    else:
        status = 'Invalid input. Try again.\n'
	if invalid_count > 3:
            status = 'Too many invalid entries. We are done here.\n'
            run = False
        invalid_count += 1



