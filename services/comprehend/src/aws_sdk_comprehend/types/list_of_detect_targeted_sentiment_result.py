"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDetectTargetedSentimentResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.batch_detect_targeted_sentiment_item_result

ListOfDetectTargetedSentimentResult: TypeAlias = list[
    "aws_sdk_comprehend.types.batch_detect_targeted_sentiment_item_result.BatchDetectTargetedSentimentItemResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDetectTargetedSentimentResult) -> list:
    import aws_sdk_comprehend.types.batch_detect_targeted_sentiment_item_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.batch_detect_targeted_sentiment_item_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDetectTargetedSentimentResult:
    import aws_sdk_comprehend.types.batch_detect_targeted_sentiment_item_result

    out: ListOfDetectTargetedSentimentResult = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.batch_detect_targeted_sentiment_item_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
