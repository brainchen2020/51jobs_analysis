# -*- coding: utf-8 -*-
from __future__ import print_function
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import sys

text = open("wc_clear.txt").read()
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)

# print()
# print('sentences:')
# for s in tr4w.sentences:
#     print(s)                 # py2中是unicode类型。py3中是str类型。
#
# print()
# print('words_no_filter')
# for words in tr4w.words_no_filter:
#     print('/'.join(words))   # py2中是unicode类型。py3中是str类型。
#
# print()
# print('words_no_stop_words')
# for words in tr4w.words_no_stop_words:
#     print('/'.join(words))   # py2中是unicode类型。py3中是str类型。
#
# print()
print('words_all_filters')
with open("wc_clear_phrase.csv",'w') as f:
    for words in tr4w.words_all_filters:
        f.write('/'.join(words))
        print("write done")   # py2中是unicode类型。py3中是str类型。
