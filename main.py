import random

def init():
    signs = ['R','P','S']
    signs_data={'R':'Rock', 'P':'Paper', 'S':'Scissors'}
    print('-------------Rock Paper Scissors Game-----------')
    isValidInput = False
    computer_choice = random.choice(signs)
    while isValidInput == False:
        print('Please Select your hand sign.\nInput R for Rock, P for Paper, S for Scissors\n')
        players_choice = input('Input your choice: ').upper()
        if players_choice in signs:
            if players_choice ==  computer_choice :
                print('Player (' + signs_data[players_choice] +') : CPU ('+signs_data[computer_choice]+')')
                print("It's a draw, Play again")
            else:
                isValidInput = True
        else:
            print('Your choice is invalid, please try again')

    print('Player (' + signs_data[players_choice] +') : CPU ('+signs_data[computer_choice]+')')
    if players_choice == 'R' and computer_choice == 'P':
        print('CPU Wins')
    elif players_choice == 'R' and computer_choice == 'S':
        print('Player Wins')
    elif players_choice == 'P' and computer_choice == 'R':
        print('Player Wins')
    elif players_choice == 'P' and computer_choice == 'S':
        print('CPU Wins')
    elif players_choice == 'S' and computer_choice == 'R':
        print('CPU Wins')
    elif players_choice == 'S' and computer_choice == 'P':
        print('Player Wins')
    
init()