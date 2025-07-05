from brain_games.cli import run_welcome_user
from brain_games.utilite import get_random_number


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def logic_games():
    name = run_welcome_user()

    for _ in range(3):
        num = get_random_number()
        answer = is_even(num)
        print(f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion: {num}')
        your_answer = input('Your answer: ')

        if answer == your_answer:
            print('Correct!')
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')

# logic_games()



