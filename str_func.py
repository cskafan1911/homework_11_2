def changes_letters_to_uppercase(value:str):
    """
    Принимает строку и возвращает со всеми заглавными буквами
    """

    return value.title()

def makes_the_first_letters_uppercase(value:str):
    """
    Делает первые буквы каждого слова заглавными
    """
    value_change = ""

    for word in value.split(" "):
        value_change += word.lower().title() + " "

    return value_change