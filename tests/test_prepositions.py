import pytest
from bennie import find_dangling_prepositions


@pytest.fixture(scope="module")
def nlp_warmup():
    """Load the spaCy model once for the entire module to avoid per-test overhead."""
    find_dangling_prepositions("warmup")


@pytest.mark.parametrize("text", [
    "What are you looking at?",
    "He knew what she was talking about.",
    "I need a pen to write with.",
    "We have something to look forward to.",
    "He got out.",
    "The person I spoke to called me back.",
])
def test_detects_dangling_preposition(nlp_warmup, text):
    found, sentences = find_dangling_prepositions(text)
    assert found is True
    assert len(sentences) > 0


@pytest.mark.parametrize("text", [
    "This is the house that Jack built.",
    "To whom did you give the book?",
    "Where are you going?",
    "She ran into the wall.",
    "He got out of the house.",
])
def test_no_dangling_preposition(nlp_warmup, text):
    found, sentences = find_dangling_prepositions(text)
    assert found is False
    assert sentences == []
