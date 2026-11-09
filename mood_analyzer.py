# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        The preprocessing keeps words, contractions, and non-ASCII symbols
        such as emojis as separate tokens while dropping ordinary punctuation.
        """
        cleaned = text.strip().lower()
        tokens = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?|[^\x00-\x7f\s]", cleaned)

        print(f"Tokens: {ascii(tokens)}")

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        Modeling improvements:
          - Handle simple negation such as "not happy", "no happy", or "not bad"
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        score, _, _, _, _ = self._analyze_text(text)
        return score

    def _analyze_text(
        self, text: str
    ) -> Tuple[int, bool, bool, List[str], List[str]]:
        """Return the score, signal flags, and matching signal tokens."""
        tokens = self.preprocess(text)
        strong_positive = {"😊": 2, "😂": 2, "🔥": 2, "💅": 2, "✨": 2, "lol": 2}
        strong_negative = {"😢": -2, "😭": -2, "💀": -2, "ugh": -2, "smh": -2}
        negations = {"not", "no", "never"}

        score = 0
        has_positive = False
        has_negative = False
        positive_hits: List[str] = []
        negative_hits: List[str] = []
        for index, token in enumerate(tokens):
            if token in strong_positive:
                signal = strong_positive[token]
            elif token in strong_negative:
                signal = strong_negative[token]
            elif token in self.positive_words:
                signal = 1
            elif token in self.negative_words:
                signal = -1
            else:
                continue

            if index > 0 and tokens[index - 1] in negations:
                signal *= -1

            if signal > 0:
                has_positive = True
                positive_hits.append(token)
            elif signal < 0:
                has_negative = True
                negative_hits.append(token)
            score += signal

        return score, has_positive, has_negative, positive_hits, negative_hits

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        If both positive and negative signals are present, return "mixed".
        """
        score, has_positive, has_negative, _, _ = self._analyze_text(text)

        if has_positive and has_negative:
            return "mixed"
        if score > 0:
            return "positive"
        if score < 0:
            return "negative"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        The explanation uses the same scoring rules as score_text() and
        predict_label(), including negation and strong emoji/slang signals.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        """
        score, _, _, positive_hits, negative_hits = self._analyze_text(text)

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
