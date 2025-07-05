import prompt

from brain_games import consts


def run_games(description, get_question_and_answer):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{description}')
    for _ in range(consts.rounds):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!")
            return 

    print(f"Congratulations, {name}!")
