"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SentimentScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.double


class SentimentScore(TypedDict, closed=True):
    positive: "aws_sdk_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>POSITIVE</code> sentiment.</p>"""
    negative: "aws_sdk_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEGATIVE</code> sentiment.</p>"""
    neutral: "aws_sdk_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEUTRAL</code> sentiment.</p>"""
    mixed: "aws_sdk_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>MIXED</code> sentiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SentimentScore) -> dict:
    out: dict = {}
    out["positive"] = value.get("positive", 0)
    out["negative"] = value.get("negative", 0)
    out["neutral"] = value.get("neutral", 0)
    out["mixed"] = value.get("mixed", 0)
    return out


def deserialize_json(data: dict) -> SentimentScore:
    out: SentimentScore = {}  # type: ignore[typeddict-item]
    if "positive" in data:
        out["positive"] = data["positive"]
    else:
        out["positive"] = 0
    if "negative" in data:
        out["negative"] = data["negative"]
    else:
        out["negative"] = 0
    if "neutral" in data:
        out["neutral"] = data["neutral"]
    else:
        out["neutral"] = 0
    if "mixed" in data:
        out["mixed"] = data["mixed"]
    else:
        out["mixed"] = 0
    return out
