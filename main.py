#!/usr/bin/env python3
"""Funniest Autocorrect Fail — one original line, 1 to 199 characters,
reading as a hilarious autocorrect slip and nothing else.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the line is built inside write_entry(); entry.txt mirrors it
# exactly. (Rev 2: dinner -> divorce is the slip — one wrong word, and
# the date never spoke to me again. The quote marks stay single so the
# line reads like a forwarded text, not a written joke.)
import os


def write_entry():
    line = (
        "I texted my date 'I had a great time, let's do dinner again "
        "soon.' Autocorrect changed dinner to 'divorce.' We have never "
        "spoken since."
    )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
