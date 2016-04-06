#!/usr/bin/env python3

import os, sys, re
from pathlib import Path


oldname = "TextSecure"
newname = "TextLibre"
re_string = re.compile(r'(?s)(<string.*?>)(.*?)(</string>)')


def string_repl(match):
    return ''.join([
        match.group(1),
        match.group(2).replace(oldname, newname),
        match.group(3)
    ])


def update_strings(f):
    oldfile = open(f).read()
    newfile = re_string.sub(string_repl, oldfile)
    with open(f, "w") as fd:
        fd.write(newfile)


def main():
    basepath = sys.argv[1]

    # Rename strings
    for p in Path(basepath).glob('**/strings.xml'):
        f = str(p)
        print(f)
        update_strings(f)


if __name__ == '__main__':
    main()
