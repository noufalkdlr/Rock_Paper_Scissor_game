import random

def win_lose(uc, cc):
    if uc == cc:
        tie = 'tie'
        return tie
    elif (uc == 'Rock' and cc == 'Paper') or (uc == "Paper" and cc == 'Scissor') or (
            uc == 'Scissor' and cc == 'Rock'):
        lose = 'lose'
        return lose

    else:
        win = 'win'
        return win

def show(uc, cc):
    print('your choice:', uc)
    print('computer choice :', cc)

def who_is_winner(u_score, c_score):
    if u_score > c_score:
        print('You are the winner')
    elif u_score == c_score:
        print('Tie....')
    else:
        print('computer is winner')

def dash():
    print('------------------------------------')

def score(sc):
    global user_score,computer_score
    if sc == 'tie':
        print('your score :', user_score,end=' | ')
        print('computer score : ', computer_score)
    elif sc == 'win':
        user_score +=1
        print('your score :',user_score,end=' | ')
        print('computer score : ',computer_score)
    else:
        computer_score +=1
        print('your score :', user_score,end=' | ')
        print('computer score : ', computer_score)

game_count = int(input('Enter game count\n'))

rps_list = ('Rock', 'Paper', 'Scissor')

user_score = 0
computer_score = 0

p_loop = 0
c_loop = 0

while p_loop<game_count and c_loop<=3:
    print('game count ',p_loop+1,'/',game_count,sep='')
    print('1.Rock', '2.Paper', '3.Scissor',sep='\n')
    user_input = input('Chose one\n')
    user_input = int(user_input) - 1

    if user_input == 0 or user_input == 1 or user_input == 2:
        computer_choice = random.choice(rps_list)
        user_choice = rps_list[user_input]
        dash()
        show(user_choice, computer_choice)
        win_or_lose = win_lose(user_choice, computer_choice)
        print(win_or_lose)
        score(win_or_lose)
        dash()
        p_loop +=1
        c_loop = 0
    else:
        c_loop += 1
        if c_loop == 1 or c_loop == 2:
            dash()
            print('please select correct one')
        elif c_loop == 3:
            warning = '''This is your last chance
please select correct one
            '''
            dash()
            print(warning)


print('Game over')
print('your score : '+str(user_score),'computer score : '+str(computer_score),sep='\n')
who_is_winner(user_score,computer_score)