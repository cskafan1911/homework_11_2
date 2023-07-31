def changes_letters_to_uppercase(value: str):
    """
    Принимает строку и возвращает со всеми заглавными буквами
    """

    return value.upper()


def makes_the_first_letters_uppercase(value: str):
    """
    Делает первые буквы каждого слова заглавными
    """
    value_change = ""

    for word in value.split(" "):
        value_change += word.lower().title() + " "

    return value_change


def sums_up_two_numbers(number_1: int, number_2: int):
    """
    Cуммирует два числа и возвращает значение суммы
    """
    summ_ = number_1 + number_2
    return summ_
