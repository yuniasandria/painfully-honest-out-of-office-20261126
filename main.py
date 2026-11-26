import os

PART_A = "I'm on vacation and my inbox already holds 214 unread emails, "
PART_B = "so I'll reply slowly on Monday with fresh eyes and honest answers."

LINE = PART_A + PART_B


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars"
    assert text.strip() != "", "entry must not be only whitespace"
    assert text.count(".") == 1 and text.strip().endswith("."), "entry must be one sentence"


if __name__ == "__main__":
    main()
