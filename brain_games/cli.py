import prompt


def run_welcome_user():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}')


if __name__ == "main()":
    run_welcome_user()