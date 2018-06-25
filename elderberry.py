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
        with open('actions.txt') as f:
            self.actions = f.read().splitlines()
        with open('all_genders_so_far.txt') as f:
            self.genders = f.read().splitlines()
        with open('locations.txt') as f:
            self.locations = f.read().splitlines()

    def insult(self):
        return random.choice(self.negative_adjectives) + ' ' + \
                random.choice(self.concrete_nouns)

    def compliment(self):
        return random.choice(self.positive_adjectives) + ' ' + \
                random.choice(self.concrete_nouns)

    def asl(self):
        a = random.randint(18, 100)
        s = random.choice(self.positive_adjectives) + ' ' + \
            random.choice(self.genders) + ' ' + \
            random.choice(self.concrete_nouns)
        l = random.choice(self.locations)
        return '{}/{}/{}'.format(a, s, l)

    def idea(self):
        noun = random.choice([self.insult(), self.compliment()])
        prefix = 'An ' if noun[:1] in 'aeiou' else 'A '
        return prefix + noun + ' ' + random.choice(self.actions)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insult Generator')
    parser.add_argument('count', type=int, nargs='?', default=1,
                        help='Number of items to generate')
    parser.add_argument('-i', '--idea', action='store_true',
                        help='Generate an \"idea\"')
    parser.add_argument('-c', '--compliment', action='store_true',
                        help='Generate a \"compliment\"')
    parser.add_argument('-a', '--asl', action='store_true',
                        help='Generate an ASL profile')
    args = parser.parse_args()

    gen = PhraseGen()
    done = 0
    while (done < args.count):
        done += 1
        if (args.idea):
            print(gen.idea())
        elif (args.asl):
            print(gen.asl())
        elif (args.compliment):
            print(gen.compliment())
        else:
            print(gen.insult())
