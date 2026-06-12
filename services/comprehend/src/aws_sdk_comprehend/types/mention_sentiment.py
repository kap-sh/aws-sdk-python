"""Generated from Smithy shape ``com.amazonaws.comprehend#MentionSentiment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.sentiment_score
    import aws_sdk_comprehend.types.sentiment_type


class MentionSentiment(TypedDict):
    sentiment: NotRequired["aws_sdk_comprehend.types.sentiment_type.SentimentType"]
    """<p>The sentiment of the mention. </p>"""
    sentiment_score: NotRequired[
        "aws_sdk_comprehend.types.sentiment_score.SentimentScore"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MentionSentiment) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> MentionSentiment:
    out: MentionSentiment = {}  # type: ignore[typeddict-item]
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
