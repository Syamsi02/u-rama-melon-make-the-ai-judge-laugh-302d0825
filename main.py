"""Make the AI Judge Laugh — one-line office joke.

Writes a single original joke about office life (one line, under
200 characters) to /output/entry.txt, where the make.fun grader
reads it, and prints it to stdout too.

Pure Python standard library; no network, no randomness, no
arguments. Running it twice produces byte-identical output.
"""

import os

JOKE = "I put 'per my last email' in my will so my family knows I meant it the first time."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Mirror of the sealed gate: UTF-8 text, 1-200 chars, one line."""
    if not text or text.isspace():
        raise ValueError("joke must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"joke is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
