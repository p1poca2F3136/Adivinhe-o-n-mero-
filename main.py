from random import randint

print('#### Iniciando Jogo ####')

random_number = randint(0, 100)
chances = 10

while chances > 0:
    user_input = input('Chute um número entre 0 a 100: ')

    if user_input.isnumeric():
        user_guess = int(user_input)
        chances -= 1

        if user_guess == random_number:
            print('\nParabéns, você venceu! O número era {} e você ainda tinha {} chances.\n'.format(random_number, chances))
            break
        else:
            print('')
            if user_guess > random_number:
                print('Você errou!!! Dica: É um número menor.')
            else:
                print('Você errou!!! Dica: É um número maior.')
            print('Você ainda possui {} chances.\n'.format(chances))
    else:
        print('\nPor favor, insira um número válido.\n')

    if chances == 0:
        print('\nSuas chances acabaram, você perdeu!\n')

print('#### Fim do Jogo ####')
