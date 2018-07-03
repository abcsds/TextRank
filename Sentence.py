#!/usr/bin/env python
import random

if __name__ == "__main__":
    filename = 'output/lk_emo.txt'
    noun = []
    verb = []
    whole_words_set = {word.rstrip() for word in open(filename)}

    for word in whole_words_set:
        if word.endswith('ing'):
            verb.append(word)
        else:
            noun.append(word)

    noun_list = list(noun)
    verb_list = list(verb)
    print(noun_list[0], verb[0], noun_list[1])
    for i in range(10):
        sentence = "%s %s %s" % (random.choice(noun_list),
                                 random.choice(verb_list),
                                 random.choice(noun_list))
        print(sentence)
