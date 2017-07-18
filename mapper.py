#!/usr/bin/env python

import sys

pattern = "https://"


def read_input(filename):
    for line in filename:
        yield line.split()


def main(separator='\t'):
    criteria = open("criteria.txt").read().splitlines()
    data = read_input(sys.stdin)
    for words in data:
        for url in words:
            if url.startswith(pattern):
                components = url.split("/")
                if len(components) == 4:
                    for c in criteria:
                        if components[3].strip("^M").startswith(c):
                            if components[3].strip("^M").endswith(c):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[3].strip("^M").endswith(c + "/"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[3].strip("^M").endswith(c + ".html"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[3].endswith(c + ".php"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                elif len(components) == 5:
                    for c in criteria:
                        if components[4].strip("^M").startswith(c):
                            if components[4].strip("^M").endswith(c):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[4].strip("^M").endswith(c + "/"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[4].strip("^M").endswith(c + ".html"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[4].strip("^M").endswith(c + ".php"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                elif len(components) == 6:
                    for c in criteria:
                        if components[5].strip("^M").startswith(c):
                            if components[5].strip("^M").endswith(c):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[5].strip("^M").endswith(c + "/"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[5].strip("^M").endswith(c + ".html"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break
                            elif components[5].strip("^M").endswith(c + ".php"):
                                print '%s%s%s' % (url.strip("^M"), separator, c)
                                break

if __name__ == "__main__":
    main()
