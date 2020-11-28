#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:31:49 2020

@author: darshayblount
"""
#Assignment 1 - Spell Checker
#lets import packages
import pandas as pd
import nltk
from nltk.corpus import words
from nltk.metrics import (edit_distance, jaccard_distance)

#correct_spellings = words.words()
#spellings_series = pd.Series(correct_spellings)

#Checks the Spelling
def SpellChecker(word: str):
    nltk.download("words") #list of words
    word = word.strip()
    rec_5 = BestFive(word)
    if word.isalpha():
        rec_5 = BestFive(word)
    else:
        rec_5 = ["Alphabetical letters only"]

#Returns the closest 5 words
def BestFive(word: str):
    dictionary = {}
    for correct_spellings in words.words():
        edit_dist = nltk.edit_distance(word, correct_spellings)
        dictionary[correct_spellings] = edit_dist
    dictionary = {keyword: dist for keyword, dist in sorted(dictionary.items(), key=lambda item: item[1])}
    count = 0
    rec_5 = []
    for key in dictionary:
        if count < 5:
            rec_5.append(key)
            count += 1
        else:
            break
    return rec_5

BestFive('limon')

