"""One-Line Roast: The Gadget You Use Every Day — entry.

Writes one roast line (at most 200 characters) to /output/entry.txt.
The target is the smartwatch: it proudly congratulates its owner
every hour for standing up, apparently unaware that the owner works
at a standing desk and the thing has been applauding furniture.
"""

import os

DEST = "/output/entry.txt"
CHAR_LIMIT = 200

ROAST = {
    "gadget": "My smartwatch",
    "behaviour": "congratulates me every hour for standing up.",
    "twist": "I work at a standing desk.",
    "sting": "It has been applauding an empty chair for two years.",
}


def line() -> str:
    order = ("gadget", "behaviour", "twist", "sting")
    text = " ".join(ROAST[key].strip() for key in order).strip()
    if not text:
        raise ValueError("a roast with no words roasts nothing")
    if len(text) > CHAR_LIMIT:
        raise ValueError(f"roast too long: {len(text)} chars over {CHAR_LIMIT}")
    if "\n" in text:
        raise ValueError("one line, one gadget, one sting")
    return text


def main() -> None:
    folder = os.path.dirname(DEST)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as fh:
        fh.write(line())


if __name__ == "__main__":
    main()
