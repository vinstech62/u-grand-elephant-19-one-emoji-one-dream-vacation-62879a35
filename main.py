#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a desert island,
the postcard version of getting away from everything.
"""

import os

ENTRY = "\U0001F3DD"  # DESERT ISLAND: my own private island, no one else invited.
OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: one single code point, inside the 1-8 character gate, not blank,
    # and actually an emoji (not a stray letter or digit that slipped in).
    if len(ENTRY) != 1:
        raise ValueError("entry must be exactly one emoji, got %d characters" % len(ENTRY))
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    code_point = ord(ENTRY)
    if not (0x1F000 <= code_point <= 0x1FAFF or 0x2600 <= code_point <= 0x27BF):
        raise ValueError("entry %r is not an emoji code point" % ENTRY)
    encoded = ENTRY.encode("utf-8")
    if not 1 <= len(encoded) <= 8:
        raise ValueError("entry must be 1-8 UTF-8 bytes, got %d" % len(encoded))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    # Read it back twice over — once as text, once as raw bytes — and confirm
    # the file holds exactly what we meant to write, nothing more.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("verification failed: file holds %r, expected %r" % (written, ENTRY))
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    if raw != encoded:
        raise ValueError("byte verification failed: file holds %r" % raw)


if __name__ == "__main__":
    main()
