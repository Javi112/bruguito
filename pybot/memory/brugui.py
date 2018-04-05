#!/usr/bin/env python
"""
 brugui.py      Pesonal stuff.
 @author:       bruguii
 @since:        05/2018
"""
import re
import sys


def brugui_utils(words):
    "Function to metion me when my name appears in a message"

    if re.search(r'(^|\s)brugui(\s|$)', words, re.I | re.M):
        return "@bruguii"


def hear(words):
    "Implements hear to receive the messages and execute the plugin logic"
    return brugui_utils(words)


def main(argv):
    "This allows to execute the plugin in standalone mode"
    if len(argv) > 1:
        print(hear(' '.join(sys.argv)))
    else:
        print('I heard nothing.')


if __name__ == "__main__":
    main(sys.argv)
