#!/usr/bin/env python

import os, sys, re
from pathlib import Path


renames = [('Signal', 'LibreSignal'),
           ('TextSecure', 'TextLibre'),
           ('RedPhone', 'PhoneLibre')]
re_string = re.compile(r'(?s)(<string.*?>)(.*?)(</string>)')


def string_repl(match):
    rename_group = match.group(2)
    for oldname, newname in renames:
        rename_group = rename_group.replace(oldname, newname)

    return ''.join([
        match.group(1),
        rename_group,
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
