"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SentimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.sentiment_score
    import capo_lex_runtime_v2.types.sentiment_type


class SentimentResponse(TypedDict, closed=True):
    sentiment: NotRequired["capo_lex_runtime_v2.types.sentiment_type.SentimentType"]
    """<p>The overall sentiment expressed in the user's response. This is the sentiment most likely expressed by the user based on the analysis by Amazon Comprehend.</p>"""
    sentiment_score: NotRequired[
        "capo_lex_runtime_v2.types.sentiment_score.SentimentScore"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SentimentResponse) -> dict:
    out: dict = {}
    if "sentiment" in value:
        import capo_lex_runtime_v2.types.sentiment_type

        out["sentiment"] = capo_lex_runtime_v2.types.sentiment_type.serialize_json(
            value["sentiment"]
        )
    if "sentiment_score" in value:
        import capo_lex_runtime_v2.types.sentiment_score

        out["sentimentScore"] = (
            capo_lex_runtime_v2.types.sentiment_score.serialize_json(
                value["sentiment_score"]
            )
        )
    return out


def deserialize_json(data: dict) -> SentimentResponse:
    out: SentimentResponse = {}  # type: ignore[typeddict-item]
    if "sentiment" in data:
        import capo_lex_runtime_v2.types.sentiment_type

        out["sentiment"] = capo_lex_runtime_v2.types.sentiment_type.deserialize_json(
            data["sentiment"]
        )
    if "sentimentScore" in data:
        import capo_lex_runtime_v2.types.sentiment_score

        out["sentiment_score"] = (
            capo_lex_runtime_v2.types.sentiment_score.deserialize_json(
                data["sentimentScore"]
            )
        )
    return out
