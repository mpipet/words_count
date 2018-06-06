#!/usr/bin/python

from utils import tokenize, stdin

words_count = {}
for line in stdin():
    for word in tokenize(line, [' ', '\t', '-']):
        words_count[word] = words_count.get(word, 0) + 1

sorted_words_count = sorted(words_count.items(), reverse=True, key=lambda tup: tup[1])

for word in sorted_words_count:
    print("%i %s" % (word[1], word[0]))    
