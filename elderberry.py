#!/usr/bin/env python3

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
        with open('locations.txt') as f:
            self.locations = f.read().splitlines()
        with open('action_verbs.txt') as f:
            self.action_verbs = f.read().splitlines()

    def insult(self):
        return random.choice(self.negative_adjectives) + ' ' + \
                random.choice(self.concrete_nouns)

    def compliment(self):
        return random.choice(self.positive_adjectives) + ' ' + \
                random.choice(self.concrete_nouns)

    def idea(self):
        noun = random.choice([self.insult(), self.compliment()])
        prefix = 'An ' if noun[:1] in 'aeiou' else 'A '
        return f"{prefix}{noun} {random.choice(self.actions)}"

    def todo(self):
        verb = random.choice(self.action_verbs).capitalize()
        noun = random.choice([self.insult(), self.compliment()])
        prefix = 'an ' if noun[:1] in 'aeiou' else 'a '
        return f"{verb} {prefix}{noun} {random.choice(self.actions)}"

    def wizard(self, level=None):
        if level is None:
            level = random.randint(0, 99) + 1
        noun = random.choice(self.concrete_nouns)
        if level >= 100:
            noun = f"{random.choice(self.positive_adjectives)} {noun}"
        if level <= -100:
            noun = f"{random.choice(self.negative_adjectives)} {noun}"

        return f"Level: {level} {noun} wizard"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Procedural content generator')
    parser.add_argument('count', type=int, nargs='?', default=1,
                        help='Number of items to generate')
    parser.add_argument('-i', '--idea', action='store_true',
                        help='Generate an \"idea\"')
    parser.add_argument('-c', '--compliment', action='store_true',
                        help='Generate a \"compliment\"')
    parser.add_argument('-t', '--todo', action='store_true',
                        help='Generate something for a todo list')
    parser.add_argument('-w', '--wizard', action='store_true',
                        help='Make a wizard class')
    parser.add_argument('-l', '--level', type=int,
                        help='Wizard level')
    args = parser.parse_args()

    gen = PhraseGen()
    done = 0
    while (done < args.count):
        done += 1
        if args.idea:
            print(gen.idea())
        elif args.compliment:
            print(gen.compliment())
        elif args.todo:
            print(gen.todo())
        elif args.wizard:
            print(gen.wizard(args.level))
        else:
            print(gen.insult())
