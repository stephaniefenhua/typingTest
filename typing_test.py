""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
def lines_from_file(path):
    f = open(path, 'r')
    lst = []
    for words in f:
        lst.append(strip(words))
    return lst

def new_sample(path, i):
    return lines_from_file(path)[i]

def analyze(sample_paragraph, typed_string, start_time, end_time):
    def wpm():
        length = len(typed_string)/5
        time = (end_time - start_time)/60
        return length/time

    def acc():
        typed, sample = split(typed_string), split(sample_paragraph)
        length = min(len(typed), len(sample))
        counter = 0
        for i in range(length):
            if typed[i] == sample[i]:
                counter += 1
        if length == 0:
            return 0.0
        return counter/length * 100
    return [wpm(), acc()]

def pig_latin(word):
    first_vowel, i = '', 0
    while first_vowel == '' and i < len(word):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            first_vowel = i
        i += 1
    if first_vowel == 0:
        return word + 'way'
    elif not first_vowel:
        return word + 'ay'
    else:
        return word[first_vowel:] + word[:first_vowel] + 'ay'

def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    return min(words_list, key=lambda word: score_function(user_input, word))

def swap_score(word1, word2):
    length = min(len(word1), len(word2))
    word1, word2 = word1[:length], word2[:length]
    if word1 == word2:
        return 0
    elif word1[0] == word2[0]:
        return swap_score(word1[1:], word2[1:])
    else:
        return swap_score(word1[1:], word2[1:]) + 1

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == word2: 
        return 0
    elif not word1 or not word2:
        return max(len(word1), len(word2))
    elif word1[0] == word2[0]:
        return score_function(word1[1:], word2[1:])   
    else:
        add_char = score_function(word2[0] + word1, word2) + 1
        remove_char = score_function(word1[1:], word2) + 1
        substitute_char = score_function(word1[1:], word2[1:]) + 1
    return min(add_char, remove_char, substitute_char)

KEY_DISTANCES = get_key_distances()

def score_function_accurate(word1, word2):
    if word1 == word2: 
        return 0
    elif not word1 or not word2:
        return max(len(word1), len(word2))
    elif word1[0] == word2[0]: 
        return score_function_accurate(word1[1:], word2[1:])
    else:
        add_char = score_function_accurate(word2[0] + word1, word2) + 1
        remove_char = score_function_accurate(word1[1:], word2) + 1
        substitute_char = (score_function_accurate(word1[1:], word2[1:]) 
        + KEY_DISTANCES[word1[0], word2[0]])
    return min(add_char, remove_char, substitute_char)

word_dict = {}
def score_function_final(word1, word2):
    if word1 == word2: # Fill in the condition
        return 0
    elif not word1 or not word2:
        return max(len(word1), len(word2))
    elif (word1, word2) in word_dict:
        return word_dict[(word1, word2)]
    elif (word2, word1) in word_dict:
        return word_dict[(word2, word1)]
    elif word1[0] == word2[0]: 
        return score_function_final(word1[1:], word2[1:])
    else:
        add_char = score_function_final(word2[0] + word1, word2) + 1
        remove_char = score_function_final(word1[1:], word2) + 1
        substitute_char = (score_function_final(word1[1:], word2[1:]) 
        + KEY_DISTANCES[word1[0], word2[0]])   
        word_dict[(word1, word2)] = min(add_char, remove_char, substitute_char)
    return word_dict[(word1, word2)]
    













# END Q7-8
