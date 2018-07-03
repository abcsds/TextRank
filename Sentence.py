#!/usr/bin/env python
import random

if __name__ == "__main__":
    filename = 'output/p&p_res.txt'
    noun = set()
    verb = set()
    whole_words_set = {word.rstrip() for word in open(filename)}

    for word in whole_words_set:
        if word.endswith('ing'):
            verb.add(word)
        else:
            noun.add(word)

    noun_list = list(noun)
    verb_list = list(verb)
    for i in range(10):
        sentence = "%s %s %s" % (random.choice(noun_list),
                                 random.choice(verb_list),
                                 random.choice(noun_list))
        print(sentence)
