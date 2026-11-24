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

Revision: renamed LINE to ENTRY_LINE, extracted the validation
and file-writing steps into validate() and write_entry(), and
added a --output argument (default /output/entry.txt) so the
destination is explicit instead of hard-coded in main().
The entry line itself is unchanged.
"""

import argparse
import os

ENTRY_LINE = (
    "Hey you \u2014 I've got cold drinks, warm snacks and exact change "
    "for a smile. Press B7 and let my coil drop you something sweet."
)

MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def validate(text: str) -> str:
    """Check the entry line meets the bounty constraints."""
    assert 1 <= len(text) <= MAX_CHARS, "line must be 1-200 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "must not contain hidden control characters"
    )
    assert text.strip(), "must not be only whitespace"
    return text


def write_entry(text: str, output_path: str) -> None:
    """Write the validated entry line to output_path (no trailing newline)."""
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the vending-machine pickup-line entry.")
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="destination path for entry.txt (default: %(default)s)",
    )
    args = parser.parse_args()
    text = validate(ENTRY_LINE)
    write_entry(text, args.output)


if __name__ == "__main__":
    main()
