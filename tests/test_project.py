from src.project import (
    count_words,
    normalize_text,
    tokenize,
    top_n_words,
)


def test_normalize_text_lowercases_text() -> None:
    assert normalize_text("Hello WORLD") == "hello world"


def test_normalize_text_removes_punctuation() -> None:
    assert normalize_text("Hello, world!") == "hello world"


def test_normalize_text_collapses_spaces() -> None:
    assert normalize_text("hello   world") == "hello world"


def test_tokenize_splits_words() -> None:
    assert tokenize("one two three") == ["one", "two", "three"]


def test_tokenize_empty_string() -> None:
    assert tokenize("") == []


def test_count_words_counts_repeated_words() -> None:
    words = ["red", "blue", "red"]
    assert count_words(words) == {"red": 2, "blue": 1}


def test_count_words_empty_list() -> None:
    assert count_words([]) == {}


def test_top_n_words_returns_most_common_items() -> None:
    counts = {"apple": 3, "banana": 1, "carrot": 2}
    assert top_n_words(counts, 2) == [("apple", 3), ("carrot", 2)]


def test_top_n_words_with_ties_sorts_alphabetically() -> None:
    counts = {"apple": 2, "banana": 2, "carrot": 1}
    assert top_n_words(counts, 2) == [("apple", 2), ("banana", 2)]


def test_top_n_words_with_non_positive_n_returns_empty_list() -> None:
    counts = {"apple": 3}
    assert top_n_words(counts, 0) == []


def test_top_n_words_n_larger_than_dict() -> None:
    counts = {"apple": 3}
    assert top_n_words(counts, 5) == [("apple", 3)]