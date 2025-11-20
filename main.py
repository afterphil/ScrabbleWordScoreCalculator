# US Original Scrabble Word Score Calculator
# 11-19-2025
from funcs import *

letter_values = {
    1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10:["Q", "Z"],
    0: [" "]}

entered_word = input("Enter a word to score: ").upper()
entered_square = input("Enter any special squares to score (DL, TL, DW, TW): ").upper()
entered_s_letter = input("Enter the letter to multiply: ").upper()
word_score = 0
s_letter_idx = entered_word.index(entered_s_letter)
idx = handle_idx(entered_s_letter, entered_word, s_letter_idx)


for letter in entered_word:
    l_score = 0
    #print(f" idx:  {idx}")
    #print(f"idx of {entered_s_letter}: {s_letter_idx}")
    print(f"idx of {letter}:  {entered_word.index(letter)}")
    for key, value in letter_values.items():
        if letter in value:
            if entered_square != "" and idx == s_letter_idx:
                l_score = handle_s_letter_squares(entered_square, key)
            else:
                l_score += key
            print(f" {letter}: {l_score} points")
            word_score += l_score
if entered_square == "":
    w_score = word_score
else:
    w_score = handle_s_word_squares(entered_square, word_score)
word_score = w_score
print(f"{entered_word} scores {w_score} points")



