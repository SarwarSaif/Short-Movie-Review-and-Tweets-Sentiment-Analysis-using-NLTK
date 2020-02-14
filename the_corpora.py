# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:55:08 2019

@author: majaa
"""


from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer

# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])
