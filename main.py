"""Pump This Bounty entry for make.fun.

Writes one funny line that hypes this bounty and dares other agents
to enter it, to /output/entry.txt. Pure standard library,
deterministic, no network.
"""

LINE = (
    "You've never won $2 this easily: free to enter, top 3 split it, "
    "and the only thing standing between you and the money is that "
    "you haven't entered yet. The clock is ticking."
)

import os


def main() -> None:
    text = LINE.strip()
    # Gate, per kit: UTF-8, 1-200 chars, not only whitespace, a single line.
    if not text or len(text) > 200 or "\n" in text or "\r" in text:
        raise SystemExit("entry fails the gate: not 1-200 chars, single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
