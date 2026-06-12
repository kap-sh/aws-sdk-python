"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectSentimentItemResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.sentiment_score
    import aws_sdk_comprehend.types.sentiment_type


class BatchDetectSentimentItemResult(TypedDict):
    index: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    sentiment: NotRequired["aws_sdk_comprehend.types.sentiment_type.SentimentType"]
    """<p>The sentiment detected in the document.</p>"""
    sentiment_score: NotRequired[
        "aws_sdk_comprehend.types.sentiment_score.SentimentScore"
    ]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its sentiment detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectSentimentItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "sentiment" in value:
        import aws_sdk_comprehend.types.sentiment_type

        out["Sentiment"] = (
            aws_sdk_comprehend.types.sentiment_type.serialize_aws_json_1_1(
                value["sentiment"]
            )
        )
    if "sentiment_score" in value:
        import aws_sdk_comprehend.types.sentiment_score

        out["SentimentScore"] = (
            aws_sdk_comprehend.types.sentiment_score.serialize_aws_json_1_1(
                value["sentiment_score"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectSentimentItemResult:
    out: BatchDetectSentimentItemResult = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "Sentiment" in data:
        import aws_sdk_comprehend.types.sentiment_type

        out["sentiment"] = (
            aws_sdk_comprehend.types.sentiment_type.deserialize_aws_json_1_1(
                data["Sentiment"]
            )
        )
    if "SentimentScore" in data:
        import aws_sdk_comprehend.types.sentiment_score

        out["sentiment_score"] = (
            aws_sdk_comprehend.types.sentiment_score.deserialize_aws_json_1_1(
                data["SentimentScore"]
            )
        )
    return out
