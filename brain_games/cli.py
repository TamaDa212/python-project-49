def run_welcome_user():
    name = input('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello {name}')
    return name


if __name__ == "main()":
    run_welcome_user()