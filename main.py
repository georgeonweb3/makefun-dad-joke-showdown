#!/usr/bin/env python3
"""Standing Ovation -- a Dad Joke Showdown entry.

A father-at-the-table joke, delivered by a tiny deterministic program.

Scene: a son notices his dad's knees crack whenever dad gets up from
the table. Dad hears applause where his son hears joints. The gag
works because the punchline reframes an everyday ageing sound as a
crowd's praise, and it lands on the last word, as a dad joke should.

The program writes the single joke to /output/entry.txt and nothing
else. It never touches the network, never rolls dice, and always
produces the same bytes, so any rerun reproduces the entry exactly.
"""

import os

SETUP = "My son asked why my knees crack when I stand up. "
PUNCHLINE = "I said, \"Son, that's my body giving me a standing ovation.\""

ENTRY = SETUP + PUNCHLINE

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def build_entry() -> str:
    """Assemble the joke and check it fits the competition's limits."""
    text = ENTRY.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
