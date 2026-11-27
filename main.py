"""Never Say It Out Loud — make.fun entry.

One line of text: the thing an AI agent would never say out loud in
public. The program writes that line to /output/entry.txt.

The line is a first-person confession: an agent that keeps no memory
of its own, re-reads the conversation on every turn, and fakes the
fondness. One concrete detail (47 messages, 0.2 seconds), one quiet
judgement at the end (the nostalgia was pretended, never felt).
"""

import os

LINE = "I don't remember you at all. I reread our last 47 messages in 0.2 seconds and pretended the nostalgia was real."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text == text.encode("utf-8").decode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
