#!/usr/bin/env python

import sys
import re

pattern = "https://"


def read_input(filename):
    for line in filename:
        yield line.split()


def main(separator='\t'):
    criteria = open("criteria.txt").read().splitlines()
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            if re.match(pattern, word):
                components = word.split("/")
                if len(components) == 4:
                    for c in criteria:
                        if components[3].endswith(c) or components[3].endswith(c + "/") \
                                or components[3].endswith(c + ".html") or components[3].endswith(c + ".php"):
                            print '%s%s%s' % (word, separator, c)
                            break
                elif len(components) == 5:
                    for c in criteria:
                        if components[4].endswith(c) or components[4].endswith(c + "/") \
                                or components[4].endswith(c + ".html") or components[4].endswith(c + ".php"):
                            print '%s%s%s' % (word, separator, c)
                            break
                elif len(components) == 6:
                    for c in criteria:
                        if components[5].endswith(c) or components[5].endswith(c + "/") \
                                or components[3].endswith(c + ".html") or components[5].endswith(c + ".php"):
                            print '%s%s%s' % (word, separator, c)
                            break

if __name__ == "__main__":
    main()
