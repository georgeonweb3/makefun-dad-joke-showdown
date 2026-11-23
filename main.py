#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.

The joke: a father-at-the-table dialogue. The son asks why dad's knees
crack every time he stands up; the punchline turns the cracking sound
into applause -- a "standing ovation" -- so the pun lands on the first
read, the setup is a classic dad scene, and the punchline arrives last.
Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "My son asked why my knees crack when I stand up. "
    "I said, \"Son, that's my body giving me a standing ovation.\""
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
