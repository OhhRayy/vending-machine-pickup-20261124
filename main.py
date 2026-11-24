"""One Line, One Minute: The Vending Machine Pickup Line Contest
(make.fun bounty u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee).

Writes a single pickup line to /output/entry.txt, spoken by a vending
machine to a passing human. Deterministic, no network, no randomness,
no input: the same line, byte for byte, on every run. The line was
chosen for the judge's brief: it is unmistakably the machine speaking
("Hey you"), it draws on the machine's own world (cold drinks, warm
snacks, exact change, button B7, the coil), the punch lands in the
last few words ("drop you something sweet"), it is short and speakable
at 124 characters, and it is cheeky and warm rather than creepy.
"""

import os

LINE = (
    "Hey you \u2014 I've got cold drinks, warm snacks and exact change "
    "for a smile. Press B7 and let my coil drop you something sweet."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. This line is 124 characters.
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
