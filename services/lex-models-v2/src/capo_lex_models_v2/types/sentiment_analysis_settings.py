"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SentimentAnalysisSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean


class SentimentAnalysisSettings(TypedDict, closed=True):
    detect_sentiment: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Sets whether Amazon Lex uses Amazon Comprehend to detect the sentiment of user utterances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SentimentAnalysisSettings) -> dict:
    out: dict = {}
    out["detectSentiment"] = value.get("detect_sentiment", False)
    return out


def deserialize_json(data: dict) -> SentimentAnalysisSettings:
    out: SentimentAnalysisSettings = {}  # type: ignore[typeddict-item]
    if "detectSentiment" in data:
        out["detect_sentiment"] = data["detectSentiment"]
    else:
        out["detect_sentiment"] = False
    return out
