import pgzrun, time
from random import randint
"""
In this game, the dancer performs a sequence of moves and you need to repeat them using your arrow keys 
generate a sequence of dance moves 
create a countdown
display moves on the screen
check if user pressed the correct buttons 
if correct, continue. if not, end game

HACKS AND TWEAKS 

make each level more complex by adding more dance moves 

play against a friend 


"""
#CONSTANTS
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
#global vars
move_list = [] #contain the dance moves
display_list = []

score = 0
score2 = 0
current_move = 0
count = 4
dance_length = 4
level = 0

#flags
say_dance = False
show_countdown = True
moves_complete = False
game_over = False
player1_turn = True

#add the actors
dancer = Actor('dancer-start')
dancer.pos = CENTER_X+5,CENTER_Y-40

up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110

right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170

down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230

left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

def draw():
    global game_over, sdcore, say_dance
    global count, show_countdown

    if not game_over:
        screen.clear()
        screen.blit('stage',(0,0))

        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()

        screen.draw.text('Player 1 Score: {}'.format(score),color='black',topleft=(WIDTH-150,10))
        screen.draw.text('Player 2 Score: {}'.format(score2), color='black', topleft=(10, 10))
        screen.draw.text('Level: {}'.format(level), color='black', topleft=(CENTER_X-25,10))
        if say_dance:
            screen.draw.text('Dance!', color='black',topleft=(CENTER_X-65,150),fontsize=60)
        if show_countdown:
            screen.draw.text('{}'.format(count), color='black',topleft=(CENTER_X-8,150),fontsize=60)
        if player1_turn: #i believe its because when the flag changes it is after generate move is called
            screen.draw.text('Player 2 Turn', color='black', topleft=(50,100),fontsize=60)
        else:
            screen.draw.text('Player 1 Turn', color='black', topleft=(CENTER_X+100, 100), fontsize=60)
    else:
        screen.clear()
        screen.blit('stage',(0,0))
        screen.draw.text('Player 1 Score: {}'.format(score), color='black', topleft=(WIDTH - 150, 10))
        screen.draw.text('Player 2 Score: {}'.format(score2), color='black', topleft=(10, 10))
        screen.draw.text("GAME OVER!", color="black",topleft=(CENTER_X - 130, 220), fontsize=60)
    return

def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = 'dancer-start'
        up.image = 'up'
        right.image = 'right'
        left.image = 'left'
        down.image = 'down'
    return

def update_dancer(move): #will update the image of the dancer to match the move paramter and highlight which arrow to press
    global game_over
    if not game_over:
        if move == 0: #if move is 'up'
            up.image = 'up-lit'
            dancer.image = 'dancer-up'
            clock.schedule(reset_dancer,0.5) #reset dancer back to normal
        if move == 1: #if move is 'right'
            right.image = 'right-lit'
            dancer.image = 'dancer-right'
            clock.schedule(reset_dancer, 0.5)  # reset dancer back to normal
        if move == 2: #if move is 'right'
            down.image = 'down-lit'
            dancer.image = 'dancer-down'
            clock.schedule(reset_dancer, 0.5)  # reset dancer back to normal
        if move == 3: #if move is 'right'
            left.image = 'left-lit'
            dancer.image = 'dancer-left'
            clock.schedule(reset_dancer, 0.5)  # reset dancer back to normal
    return

def display_moves():
    global display_list, say_dance, show_countdown
    if display_list: #if there are moves in the display list
        this_move = display_list[0] #current move is the first item in the list
        display_list = display_list[1:] # removes the first first item from display list
        #or
        #display_list = display_list.pop(0)
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves,1) #will display the next move 1 second RECURSIVE FUNCTION
        if this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1)
        if this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves, 1)
        if this_move == 3:
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True #tells draw() to change
        show_countdown = False
    return

def generate_moves():
    global move_list, display_list, show_countdown, count,say_dance, level, dance_length, player1_turn
    rand_num = 0
    #print("the level is {} and the dance_length {}".format(level, dance_length))

    if player1_turn:
        dance_length = dance_length + level
    move_list = []
    say_dance = False
    for index in range(dance_length):
        rand_num = randint(0,3)
        move_list.append(rand_num)
        display_list.append(rand_num)
    show_countdown = True
    countdown()
    print('move_list={}'.format(move_list))
    if player1_turn:
        level+=1
        player1_turn = False
    else:
        player1_turn = True
    return

def countdown():
    global count, show_countdown
    if count > 1:
        count-=1
        clock.schedule(countdown,1)
    else:
        show_countdown = False
        display_moves()
    return

def next_move():
    global current_move, moves_complete
    if current_move < dance_length-1:
        current_move += 1
    else:
        moves_complete = True
    return

def on_key_up(key):
    global score,game_over,move_list,current_move,score2
    if key == keys.UP:
        update_dancer(0)
        if move_list[current_move] == 0:
            score +=1
            next_move()
        else:
            game_over = True
    if key == keys.RIGHT:
        update_dancer(1)
        if move_list[current_move] == 1:
            score +=1
            next_move()
        else:
            game_over = True
    if key == keys.DOWN:
        update_dancer(2)
        if move_list[current_move] == 2:
            score +=1
            next_move()
        else:
            game_over = True
    if key == keys.LEFT:
        update_dancer(3)
        if move_list[current_move] == 3:
            score +=1
            next_move()
        else:
            game_over = True

    if key == keys.W:
        update_dancer(0)
        if move_list[current_move] == 0:
            score2 +=1
            next_move()
        else:
            game_over = True
    if key == keys.D:
        update_dancer(1)
        if move_list[current_move] == 1:
            score2 +=1
            next_move()
        else:
            game_over = True
    if key == keys.S:
        update_dancer(2)
        if move_list[current_move] == 2:
            score2 +=1
            next_move()
        else:
            game_over = True
    if key == keys.A:
        update_dancer(3)
        if move_list[current_move] == 3:
            score2 +=1
            next_move()
        else:
            game_over = True
    return

def update():
    global current_move, moves_complete
    if not game_over:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
        music.stop()


generate_moves()
music.play('vanishing-horizon')
pgzrun.go()