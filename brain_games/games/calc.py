from random import choice, randint

DESCRIPTION = "What is the result of the expression?"

OPERATORS = ("+", "-", "*")


def get_round():
    first_number = randint(1, 20)
    second_number = randint(1, 20)
    operator = choice(OPERATORS)

    question = f"{first_number} {operator} {second_number}"

    match operator:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number

    return question, str(result)
