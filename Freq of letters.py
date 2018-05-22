import re


def freq_letters(target_dict, target_text):
    for letter in target_text:
        if letter in target_dict:
            target_dict[letter] = target_dict.get(letter) + 1
        else:
            target_dict[letter] = 1


file = open("charter.txt", "r")
pure_string = []
dictionary = {}
for line in file:
    pure_string += re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?1234567890 \n•—«»…]', line)
all_file = ''.join(pure_string)
freq_letters(dictionary, all_file.lower())
sorted_letters = sorted(dictionary, key=dictionary.get, reverse=True)
print(len(dictionary))
for ch in sorted_letters:
    print( dictionary[ch])

