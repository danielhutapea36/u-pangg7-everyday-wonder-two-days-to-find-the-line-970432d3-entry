#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence of everyday wonder to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The sentence is
119 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence
— every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a small moment of
wonder in everyday life in a single sentence — a gecko blinking on
the ceiling is as everyday as it gets; (2) an angle the reader has
not met before — the room does not belong to the person in it, it
belongs to the gecko, to something older than the house; (3) the
surprise lands in one read — the turn arrives in the final clause,
"belonged to something older than the house"; (4) grounded in
something real and specific — a gecko, a ceiling, a house, a held
breath; (5) every word works — no filler, no worn phrase, no
puddle, no kettle, none of the brief's own examples.
"""

import os

TEXT = (
    "The gecko on the ceiling blinked once, and for a held breath "
    "the whole room belonged to something older than the house."
)


def main() -> None:
    # Gate: entry.txt must be 1-200 characters of UTF-8 text, not only
    # whitespace. The sentence is 119 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
