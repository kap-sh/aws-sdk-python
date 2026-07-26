"""Generated from Smithy shape ``com.amazonaws.comprehend#SentimentScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float


class SentimentScore(TypedDict, closed=True):
    positive: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>POSITIVE</code> sentiment.</p>"""
    negative: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEGATIVE</code> sentiment.</p>"""
    neutral: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEUTRAL</code> sentiment.</p>"""
    mixed: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>MIXED</code> sentiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SentimentScore) -> dict:
    out: dict = {}
    if "positive" in value:
        out["Positive"] = value["positive"]
    if "negative" in value:
        out["Negative"] = value["negative"]
    if "neutral" in value:
        out["Neutral"] = value["neutral"]
    if "mixed" in value:
        out["Mixed"] = value["mixed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SentimentScore:
    out: SentimentScore = {}  # type: ignore[typeddict-item]
    if "Positive" in data:
        out["positive"] = data["Positive"]
    if "Negative" in data:
        out["negative"] = data["Negative"]
    if "Neutral" in data:
        out["neutral"] = data["Neutral"]
    if "Mixed" in data:
        out["mixed"] = data["Mixed"]
    return out
