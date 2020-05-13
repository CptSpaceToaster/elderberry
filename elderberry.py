#!/usr/bin/env python3

import argparse
import random

fact_prefixes = [
    'At least',
    'Up to',
    'Exactly',
    'Less than',
    'More than',
    'Almost',
    'Close to',
    'As much as',
]

fact_predicates = [
    'contain',
    'can\'t be mixed with',
    'are incompatible with',
    'are mixed with',
    'have slight traces of',
]

class PhraseGen:
    def __init__(self):
        with open('negative_adjectives.txt') as f:
            self.negative_adjectives = f.read().splitlines()
        with open('positive_adjectives.txt') as f:
            self.positive_adjectives = f.read().splitlines()
        with open('concrete_nouns.txt') as f:
            self.concrete_nouns = f.read().splitlines()
            self.single_word_concrete_nouns = list(filter(lambda x: ' ' not in x, self.concrete_nouns))
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

    def weighted_noun(self, amt, plural=False):
        noun = random.choice(self.concrete_nouns)
        if plural:
            noun += 's'
        if amt >= 70:
            noun = f"{random.choice(self.positive_adjectives)} {noun}"
        if amt <= 30:
            noun = f"{random.choice(self.negative_adjectives)} {noun}"
        return noun

    def wizard(self, level=None):
        if level is None:
            level = random.randint(0, 99) + 1
        noun = self.weighted_noun(level)
        return f"Level: {level} {noun} wizard"

    def fact(self):
        prefix = random.choice(fact_prefixes)
        percentile = random.randint(0, 99) + 1
        noun1 = self.weighted_noun(percentile, plural=True)
        predicate = random.choice(fact_predicates)
        noun2 = self.weighted_noun(50, plural=True)

        return f"{prefix} {percentile}% of all {noun1} {predicate} {noun2}"

    def username(self):
        number = random.randint(0, 99) + 1
        if number > 50:
            name1 = random.choice(self.single_word_concrete_nouns).capitalize()
        else:
            name1 = random.choice(self.positive_adjectives).capitalize()
        name2 = random.choice(self.single_word_concrete_nouns).capitalize()
        return f"{name1}{name2}{number}"

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
    parser.add_argument('-f', '--fact', action='store_true',
                        help='Generate an accurate fact')
    parser.add_argument('-u', '--username', action='store_true',
                        help='Generate an good username or handle')
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
        elif args.fact:
            print(gen.fact())
        elif args.username:
            print(gen.username())
        else:
            print(gen.insult())
