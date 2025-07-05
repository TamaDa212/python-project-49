import math

from brain_games import engine
from brain_games.consts import description_gcd
from brain_games.utilite import get_random_number


def get_question_and_answer():
    number1, number2 = get_random_number(), get_random_number()
    correct_answer = str(math.gcd(number1, number2))

    question = f'{number1} {number2}'
    return question, correct_answer 


def run_game_gcd():
    engine.run_games(description_gcd, get_question_and_answer)