#!/usr/bin/env python
"""
 sentences.py   Returns a random sentence of the stored in sentences.json
 Author:        Alejandro Brugarolas
 Date:          2018/10
"""

from __future__ import print_function

import os
import re
import sys
import random
import json


SENTENCES_FILE = os.path.join(os.path.dirname(__file__), "utilities.json")


def sentence(message):
    "Listens to choice command and returns a random choice from words."
    with open(SENTENCES_FILE) as datafile:
        sentences = json.load(datafile)
    return random.choice(sentences["sentences"])

def frase(message):
    return sentence(message)


def main(argv):
    "This allows to execute the plugin in standalone mode"
    if len(argv) > 1:
        print(sentence(' '.join(sys.argv)))
    else:
        print('I heard nothing.')


if __name__ == "__main__":
    main(sys.argv)
