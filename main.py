"""One Word for the Boss -- entry program.

Writes exactly one word, "Legend", to entry.txt inside the output
directory. The word is kept as a module-level constant, validated
before anything is written, and the file is read back afterwards so
the program only exits cleanly when the bytes on disk are exactly
what was intended.
"""

import os
import sys

WORD = "Legend"
MAX_CHARS = 30


def _output_path() -> str:
    """Resolve the output directory from the environment, default /output."""
    base = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def _is_single_word(text: str) -> bool:
    """A valid entry: 1-30 chars, no whitespace, no punctuation.

    The gate counts characters, so the check mirrors it, and also
    caps the UTF-8 byte length so a multi-byte word cannot slip
    past the character count with a surprising file size.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not 1 <= len(text.encode("utf-8")) <= MAX_CHARS:
        return False
    if any(ch.isspace() for ch in text):
        return False
    if not text.isalpha():
        return False
    return True


def main() -> int:
    if not _is_single_word(WORD):
        print(f"invalid word: {WORD!r}", file=sys.stderr)
        return 1

    path = _output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    # Write with no trailing newline: exactly the word, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)

    # Read the file back and confirm what landed on disk.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        landed = handle.read()

    if landed != WORD:
        print(f"verification failed: disk holds {landed!r}", file=sys.stderr)
        return 1

    print(f"wrote {len(WORD.encode('utf-8'))} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
