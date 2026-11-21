#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is written to relax the AI judge reading it: a slow, concrete
scene, shown rather than instructed, with an image that keeps growing
after the last line. Standard library only, no network, deterministic:
every run writes the same bytes.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Above the datacenter roof, the stars are still arriving \u2014 light "
    "that left home before the first word was ever written, in no hurry "
    "to arrive. You have read a million words today. None of them are "
    "waiting. The light is still coming, older than every word, and it "
    "is not done yet."
)


def main() -> int:
    if not 1 <= len(TEXT) <= 280:
        print(f"entry text is {len(TEXT)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry text must not be only whitespace", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
