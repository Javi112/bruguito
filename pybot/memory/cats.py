#!/usr/bin/env python
"""
 rael.py        Pesonal stuff.
 Author:        Rael Garcia <self@rael.io>
 Date:          06/2016
 Tested on:     Python 3 / OS X 10.11.5
"""

import re
import sys
import random


def get_cat_gif():
    """Gets a random cat from catapi"""

    cat_apiurl = "http://thecatapi.com/api/images/get?format=src&type=gif"

    return cat_apiurl + "&timestamp=" + str(random.random()) + ".gif"

def cat(message):
    """Checks if the word Cat exists in the string"""
    return get_cat_gif()

def gato(message):
    return cat(message)

def main(argv):
    "This allows to execute the plugin in standalone mode"
    if len(argv) > 1:
        print(cat(' '.join(sys.argv)))
    else:
        print('I heard nothing.')


if __name__ == "__main__":
    main(sys.argv)
