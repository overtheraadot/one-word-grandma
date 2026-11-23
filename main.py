"""One Word From Grandma — entry program.

Writes exactly one word to entry.txt: the word grandma would text about AI.
Deterministic, no network, no model calls, no file reads outside the repo.
"""

import os

WORD = "robott"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
