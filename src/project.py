"""Project 1 starter: Data Detective.

Implement the required functions below.
Use standard library only.
"""

from __future__ import annotations

from pathlib import Path
import string


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def normalize_text(text: str) -> str:
    """Return a normalized version of the text.

    - lowercase the text
    - remove punctuation
    - collapse extra whitespace
    """
    # Lowercase
    text = text.lower()

    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)

    # Collapse whitespace
    text = " ".join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    """Split normalized text into a list of words."""
    if not text:
        return []
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count how many times each word appears."""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top N words as (word, count) tuples."""
    if n <= 0:
        return []

    # Sort by count descending, then alphabetically
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    return sorted_words[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> object:
    """Return one extra insight of your choice.

    Here: average word length
    """
    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    avg_length = total_length / len(words)

    return round(avg_length, 2)


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run the full analysis pipeline and return summary data."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    demo_path = Path("data/sample.txt")
    if demo_path.exists():
        results = run_demo(str(demo_path), n=10)
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print("No demo file found at data/sample.txt")