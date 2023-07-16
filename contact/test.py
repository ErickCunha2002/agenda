# flake8: noqa

def to_jaden_case(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    new_string = ' '.join(capitalized_words)
    return new_string

print(to_jaden_case('hello world eu sou feliz'))