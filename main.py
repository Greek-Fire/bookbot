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


file_path = './books/frankenstein.txt'
print(word_count(file_path))
print(letter_count(file_path))