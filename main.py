def read_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def word_count(file_path):
    file_str = read_file(file_path)
    count = len(file_str.split())
    return count

def letter_count(file_path):
    
    char_dict = {}
    file_str = read_file(file_path)

    for char in file_str:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    # sort dictionary by key
    char_dict = dict(sorted(char_dict.items()))
    return char_dict

def get_report(letter_dict):
    
    wc = word_count(file_path)

    print(f'\n--- Begin report of {file_path} ---\n')
    print(f'Total word count: {wc}')

    for key, value in letter_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found '{value}' times")

    print(f'\n--- End report of {file_path} ---\n')

file_path = './books/frankenstein.txt'

letter_dict = letter_count(file_path)
get_report(letter_dict)
