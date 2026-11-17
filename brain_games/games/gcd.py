from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."


def calculate_gcd(first_number, second_number):
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )

    return first_number


def get_round():
    first_number = randint(1, 100)
    second_number = randint(1, 100)

    question = f"{first_number} {second_number}"
    correct_answer = calculate_gcd(first_number, second_number)

    return question, str(correct_answer)
