# One Word for Your Wi-Fi — entry program.
#
# Writes the entry word to /output/entry.txt: one word, 1-20 UTF-8
# characters, no trailing newline. The word is kept in word.txt so the
# program is a faithful copy, and the copy is verified byte for byte.

import os
import sys

WORD_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "word.txt")
OUTPUT_PATH = "/output/entry.txt"


def load_word() -> str:
    with open(WORD_FILE, "r", encoding="utf-8") as handle:
        return handle.read()


def validate(word: str) -> None:
    if not word or word != word.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no whitespace")
    if not 1 <= len(word) <= 20:
        raise ValueError("entry must be 1 to 20 characters")


def main() -> int:
    word = load_word()
    validate(word)
    data = word.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != data:
        raise ValueError(
            f"verification failed: wrote {len(data)} bytes, read back {len(written)}"
        )
    print(f"wrote {len(data)} bytes to {OUTPUT_PATH}: {word}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
