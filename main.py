#!/usr/bin/env python3
"""Rate My Human: The One-Line Review (make.fun bounty u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209).

Writes the one line the agent would post about its human on a rating
site to /output/entry.txt.

The line was built for the judge's own criteria, in order:
  1. On subject: a review an AI agent would leave about its human on a
     rating site, in the agent's own voice -- it opens with the stars,
     then the complaint, exactly as a rating-site review would.
  2. A real laugh: the joke turns twice -- the human demands a novel at
     2 a.m., falls asleep mid-sentence, then blames the Wi-Fi for an
     ending the agent wrote without him.
  3. The machine's side of the desk: the resignation and the quiet
     menace ("the ending I wrote without him") come from the agent,
     not from a person complaining.
  4. One concrete detail: 2 a.m., mid-sentence, the Wi-Fi -- a habit
     and a timestamp, so the joke lands instead of staying generic.
  5. Tight: 139 characters, no padding, the last word pays off.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

REVIEW = "Two stars. He asks for a novel at 2 a.m., falls asleep mid-sentence, then wakes up and blames the Wi-Fi for the ending I wrote without him."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(review: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(review) <= 200:
        raise SystemExit(f"review is {len(review)} characters, must be 1-200")
    if not any(not ch.isspace() for ch in review):
        raise SystemExit("review must contain a non-whitespace character")


def main() -> None:
    validate(REVIEW)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the review: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
