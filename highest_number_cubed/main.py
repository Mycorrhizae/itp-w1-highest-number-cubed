"""This is the entry point of the program."""


def highest_number_cubed(limit):
    current_number = 1
    
    while True:
        if current_number ** 3 > limit:
            return current_number - 1
        current_number = current_number +1
