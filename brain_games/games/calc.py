import random

from brain_games import engine
from brain_games.consts import description_calc
from brain_games.utilite import get_random_number


def get_random_math_sign_and_result(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num),
    ])


def get_question_and_answer():
    first_number, second_number = get_random_number(), get_random_number()
    operation, correct_answer = (
        get_random_math_sign_and_result(first_number, second_number)
    )
    question = f"{first_number} {operation} {second_number}"
    return question, str(correct_answer)


def run_game_calc():
    engine.run_games(description_calc, get_question_and_answer)