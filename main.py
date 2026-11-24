#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single original sentence pitching a ridiculous invention that
fixes a tiny everyday annoyance, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output). Stdlib only, no arguments, no network,
deterministic: the same bytes on every run.
"""

import os
import sys

LINE = (
    "A fridge that turns its light off and pretends to be empty every time "
    "you open it after midnight, so late-night snacking requires negotiating "
    "with an appliance in denial."
)

MAX_CHARS = 220


def validate(line: str) -> None:
    """Check the pitch is one sentence of 1-220 characters."""
    if not line or line != line.strip():
        raise ValueError("pitch must be non-empty with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("pitch must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"pitch must be 1-{MAX_CHARS} characters, got {len(line)}")
    terminators = sum(line.count(c) for c in ".!?")
    if terminators != 1 or not line.endswith("."):
        raise ValueError("pitch must be exactly one sentence ending in a period")


def main() -> int:
    if len(sys.argv) != 1:
        raise SystemExit("main.py takes no arguments")
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify the written file is exactly the pitch.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE or len(written.encode("utf-8")) != len(LINE.encode("utf-8")):
        raise ValueError("read-back mismatch: entry.txt does not match the pitch")
    print(f"Wrote {len(LINE)}-character pitch to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
