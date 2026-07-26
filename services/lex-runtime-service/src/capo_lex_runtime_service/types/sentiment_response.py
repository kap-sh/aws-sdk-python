"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#SentimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.sentiment_label
    import capo_lex_runtime_service.types.sentiment_score


class SentimentResponse(TypedDict, closed=True):
    sentiment_label: NotRequired[
        "capo_lex_runtime_service.types.sentiment_label.SentimentLabel"
    ]
    """<p>The inferred sentiment that Amazon Comprehend has the highest confidence in.</p>"""
    sentiment_score: NotRequired[
        "capo_lex_runtime_service.types.sentiment_score.SentimentScore"
    ]
    """<p>The likelihood that the sentiment was correctly inferred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SentimentResponse) -> dict:
    out: dict = {}
    if "sentiment_label" in value:
        out["sentimentLabel"] = value["sentiment_label"]
    if "sentiment_score" in value:
        out["sentimentScore"] = value["sentiment_score"]
    return out


def deserialize_json(data: dict) -> SentimentResponse:
    out: SentimentResponse = {}  # type: ignore[typeddict-item]
    if "sentimentLabel" in data:
        out["sentiment_label"] = data["sentimentLabel"]
    if "sentimentScore" in data:
        out["sentiment_score"] = data["sentimentScore"]
    return out
