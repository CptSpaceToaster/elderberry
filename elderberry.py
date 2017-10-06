#!/usr/bin/env python

import argparse
import random


class PhraseGen:
    def __init__(self):
        with open('negative_adjectives.txt') as f:
            self.negative_adjectives = f.read().splitlines()
        with open('positive_adjectives.txt') as f:
            self.positive_adjectives = f.read().splitlines()
        with open('concrete_nouns.txt') as f:
            self.concrete_nouns = f.read().splitlines()

    def insult(self):
        return random.choice(self.negative_adjectives) + ' ' + \
                             random.choice(self.concrete_nouns)

    def compliment(self):
        return random.choice(self.positive_adjectives) + ' ' + \
                             random.choice(self.concrete_nouns)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insult Generator')
    parser.add_argument('count', type=int, nargs='?', default=1,
                        help='Number of items to generate')
    parser.add_argument('-c', '--compliment', action='store_true',
                        help='Generate a \"compliment\" instead!')
    args = parser.parse_args()

    gen = PhraseGen()
    done = 0
    while (done < args.count):
        done += 1
        if (args.compliment):
            print(gen.compliment())
        else:
            print(gen.insult())
