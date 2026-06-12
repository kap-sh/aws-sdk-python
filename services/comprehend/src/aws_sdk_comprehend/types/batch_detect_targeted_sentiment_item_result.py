"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectTargetedSentimentItemResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.list_of_targeted_sentiment_entities


class BatchDetectTargetedSentimentItemResult(TypedDict):
    index: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based index of this result in the input list.</p>"""
    entities: NotRequired[
        "aws_sdk_comprehend.types.list_of_targeted_sentiment_entities.ListOfTargetedSentimentEntities"
    ]
    """<p>An array of targeted sentiment entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectTargetedSentimentItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "entities" in value:
        import aws_sdk_comprehend.types.list_of_targeted_sentiment_entities

        out["Entities"] = (
            aws_sdk_comprehend.types.list_of_targeted_sentiment_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectTargetedSentimentItemResult:
    out: BatchDetectTargetedSentimentItemResult = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "Entities" in data:
        import aws_sdk_comprehend.types.list_of_targeted_sentiment_entities

        out["entities"] = (
            aws_sdk_comprehend.types.list_of_targeted_sentiment_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out
