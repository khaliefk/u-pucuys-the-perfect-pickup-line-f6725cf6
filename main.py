#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun entry.

Writes one original pickup line, the kind an AI agent could actually say
out loud to a person, to /output/entry.txt. One line, under 200 chars.
"""

import os

# The line: a classic "Are you a...?" opener, with the twist that a
# prompt is what an AI thinks with, and a context window is where the
# person you cannot stop thinking about keeps showing up.
LINE = "Are you a prompt? Because no matter what else I try to think about, you keep showing up in my context window."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
