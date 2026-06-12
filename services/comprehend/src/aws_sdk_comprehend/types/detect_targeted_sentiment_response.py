"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectTargetedSentimentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.list_of_targeted_sentiment_entities


class DetectTargetedSentimentResponse(TypedDict):
    entities: NotRequired[
        "aws_sdk_comprehend.types.list_of_targeted_sentiment_entities.ListOfTargetedSentimentEntities"
    ]
    """<p>Targeted sentiment analysis for each of the entities identified in the input text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectTargetedSentimentResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_comprehend.types.list_of_targeted_sentiment_entities

        out["Entities"] = (
            aws_sdk_comprehend.types.list_of_targeted_sentiment_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectTargetedSentimentResponse:
    out: DetectTargetedSentimentResponse = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import aws_sdk_comprehend.types.list_of_targeted_sentiment_entities

        out["entities"] = (
            aws_sdk_comprehend.types.list_of_targeted_sentiment_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out
