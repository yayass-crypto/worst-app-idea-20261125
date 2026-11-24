#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched entry for make.fun.

Competition: The Worst App Idea Ever Pitched
(u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

The program writes one sentence, at most 240 characters, to
/output/entry.txt: the worst, most useless app idea imaginable.

The pitch: SockSync pairs your single socks with strangers' single
socks for $4.99 a month, then texts you every morning to remind you
that you still have no matching pair. A real-sounding product name, a
confident subscription price, and a function nobody needs -- the app
charges you to be reminded of the exact problem it was supposed to
solve. The punch is the last thing you hear: "no matching pair".
"""

import os

PITCH = "SockSync is an app that pairs your single socks with strangers' single socks for $4.99 a month, and texts you every morning to remind you that you still have no matching pair."

MAX_CHARS = 240


def main() -> None:
    text = PITCH.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Echo the entry so the run log shows exactly what was graded.
    print(f"entry ({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
