# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:48:03 2019

@author: majaa
"""

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
####### It's almost like stem
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("pytho"))
print(lemmatizer.lemmatize("better", pos="a")) ## "a" - adjective
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v')) ## "v" > verb