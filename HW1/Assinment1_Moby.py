#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:50:05 2020

@author: darshayblount
"""
#Assignment 1 - Moby Dick
#lets import packages
from pathlib import Path
import nltk as nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from pathlib import Path
moby = Path('/Users/darshayblount/Documents/1 MSDA/Text Mining/moby.txt').read_text()

#verfiy import
#print(moby) 

#1. Counting tokens
nltk_tokens = nltk.word_tokenize(moby)
total_tokens = "The total number of tokens is " + str(len(nltk_tokens)) #255018
print(total_tokens)
unique_tokens = nltk.FreqDist(nltk_tokens)
unique_number = "The unique number of tokens is " + str(len(unique_tokens)) #20754
print(unique_number)

#2. Lemmatization
#if verb abv in lemma_tokens

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
lemmatizer = nltk.WordNetLemmatizer()
lemma_tokens = nltk.pos_tag(nltk_tokens)
#    verbs = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] #abreviations for verbs

from collections import Counter
counts = Counter(tag for word,tag in lemma_tokens if tag in('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'))
counts #number of tokens for each verb type
number_verb = 5112 + 3517 +8786 + 4858 + 6884 + 4283
number_verb #sum of all verb types
print("The total number of verb tokens is " + str(number_verb))

#need to make the verbs their own list, then do unique tokens
just_verbs = [tag for word, tag in lemma_tokens if tag in('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')]
#verb list!
verbs_with_tag = [word for word, tag in lemma_tokens if tag in('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')]
unique_verb_tokens = nltk.FreqDist(verbs_with_tag) #5774
print("The unique number of verb tokens is " + str(len(unique_verb_tokens)))
      
#3. What percentage of tokens is 'HISTORY' or 'history'?
import re

#lowercase 'history'
def lcFilter(datalist):
    return [val for val in datalist
            if re.search(r'^history', val)]
lc_history = lcFilter(nltk_tokens)
Counter(lc_history) #15

#uppercase 'HISTORY'
def ucFilter(datalist):
    return [val for val in datalist
            if re.search(r'^HISTORY', val)]
uc_history = ucFilter(nltk_tokens)
Counter(uc_history) #4

percent = ((15+4)/255018)*100
percent #percentage of 'history' and 'HISTORY'

#4. 1.	What are the 10 most frequently occurring (unique) tokens in the text? What is their frequency?
most_freq = unique_tokens.most_common(10)
most_freq



