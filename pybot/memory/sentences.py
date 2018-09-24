#!/usr/bin/env python
"""
 sentences.py    Returns a random sentence of the storeds in sentences.json
 Author:        Rael Garcia <self@rael.io>
 Date:          06/2016
 Tested on:     Python 3 / OS X 10.11.5
"""

from __future__ import print_function

import os
import re
import sys
import random
import json


SENTENCES_FILE = os.path.join(os.path.dirname(__file__), "sentences.json")


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
