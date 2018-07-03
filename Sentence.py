#!/usr/bin/env python
# vim: set fileencoding=utf-8 ts=4 sw=4 tw=72 :

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import random

if __name__ == "__main__":
    filename = 'results.txt'
    noun = set()
    verb = set()
    whole_words_set = {word.rstrip() for word in open(filename)}

    for word in whole_words_set:
        if word.endswith('ment'):
            noun.add(word)
        elif word.endswith('ing'):
            if word[:-3] in whole_words_set:
                verb.add(word[:-3])
            elif word[:-3]+"e" in whole_words_set:
                verb.add(word[:-3]+"e")
    noun_list = list(noun)
    verb_list = list(verb)
    while True:
        sentence = "%s %s %s" % (random.choice(noun_list),
                                 random.choice(verb_list),
                                 random.choice(noun_list))
        print(sentence)
        if input("Produce more? (Y/N)").lower() == "n":
            break