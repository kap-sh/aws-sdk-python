"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectSentimentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.sentiment_score
    import aws_sdk_comprehend.types.sentiment_type


class DetectSentimentResponse(TypedDict):
    sentiment: NotRequired["aws_sdk_comprehend.types.sentiment_type.SentimentType"]
    """<p>The inferred sentiment that Amazon Comprehend has the highest level of confidence in.</p>"""
    sentiment_score: NotRequired[
        "aws_sdk_comprehend.types.sentiment_score.SentimentScore"
    ]
    """<p>An object that lists the sentiments, and their corresponding confidence levels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectSentimentResponse) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> DetectSentimentResponse:
    out: DetectSentimentResponse = {}  # type: ignore[typeddict-item]
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
