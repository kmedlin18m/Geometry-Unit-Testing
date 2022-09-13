import random

def main():
    print('----------------------')
    print('Rock - Paper - Scissor')
    print('----------------------')
    computer_list = ['rock', 'paper', 'scissor']
    comp = (random.choice(computer_list))
    random.seed(1)
    game_round = 1
    comp_score = 0
    user_score = 0
    while True:
        response = input("Enter response: ").strip().lower()
        while response not in ['rock', 'paper', 'scissor']:
            response = input('Enter a valid response: ').strip().lower()
        if response == comp:
            print('Computer is {}. You are {}. You Tie.'.format(comp, response))
        elif response == 'rock':
            if comp == 'scissor':
                print('Computer is {}. You are {}. You Win.'.format(comp, response))
                user_score += 1
            else:
                print('Computer is {}. You are {}. You Lose.'.format(comp, response))
                comp_score += 1
        elif response == 'paper':
            if comp == 'rock':
                print('Computer is {}. You are {}. You Win.'.format(comp, response))
                user_score += 1
            else:
                print('Computer is {}. You are {}. You Lose.'.format(comp, response))
                comp_score = comp_score + 1
        elif response == 'scissor':
            if comp == 'paper':
                print('Computer is {}. You are {}. You Win.'.format(comp, response))
                user_score += 1
            else:
                print('Computer is {}. You are {}. You Lose.'.format(comp, response))
                comp_score += 1
        if comp_score >= 2 or (round == 3 and comp_score > user_score):
            print('GAME OVER. YOU LOSE')
            break
        if user_score >= 2 or (round == 3 and user_score > comp_score):
            print('GAME OVER. YOU WIN')
            break
        if round == 3 and (comp_score == user_score):
            print('GAME OVER. TIE.')
        game_round = game_round + 1


if __name__ == '__main__':
    main()
