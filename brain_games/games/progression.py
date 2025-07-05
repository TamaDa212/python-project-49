from brain_games import engine
from brain_games.consts import description_progression
from brain_games.utilite import get_random_number, get_random_progression_index


def get_question_and_answer():
    first_number = get_random_number()
    progression_number = get_random_number()
    hidden_index = get_random_progression_index()

    progression = [first_number + i * progression_number for i in range(10)]
    correct_answer = progression[hidden_index]

    question = ' '.join(".." if i == hidden_index else str(num) for i,
                        num in enumerate(progression))
    
    return question, str(correct_answer)


def run_progression_game():
    engine.run_games(description_progression, get_question_and_answer)