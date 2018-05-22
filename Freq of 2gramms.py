import re
import math


def build_table(target_dict, sorted_dict, page):
    tables = open(page, "w")
    tables.write("<style>table {float: left;}</style>")
    i = 0
    cols = math.floor(len(target_dict) / 6)
    for j, ch in enumerate(sorted_dict):
        if i == 0:
            tables.write("<table>")
        tables.write(
            "<tr><td>" + str(j) + ". " + ch + "</td><td>" + str(target_dict[ch] / len(target_dict)) + "</td></tr>")
        if i == cols:
            tables.write("</table><table>")
            i = 0
        i += 1
    tables.write("</table>")


def freq_bigramms(target_text):
    words = target_text.split()
    dictionary = {}
    for word in words:
        i = 0
        while i < len(word) - 1:
            if word[i]+word[i+1] in dictionary:
                dictionary[word[i]+word[i+1]] = dictionary.get(word[i]+word[i+1]) + 1
            else:
                dictionary[word[i]+word[i+1]] = 1
            i += 1
    return dictionary


file = open("alco.txt", "r")
pure_string = []
dictionary = {}
for line in file:
    pure_string += re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?1234567890•—«»…]', line)
all_file = ''.join(pure_string)
text = all_file.replace("\n", " ").lower()
print(text)
dictionary = freq_bigramms(text)
sorted_bigramms = sorted(dictionary, key=dictionary.get, reverse=True)
build_table(dictionary, sorted_bigramms, "tables.txt")




