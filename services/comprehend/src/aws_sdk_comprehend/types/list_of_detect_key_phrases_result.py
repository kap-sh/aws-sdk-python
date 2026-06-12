"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDetectKeyPhrasesResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.batch_detect_key_phrases_item_result

ListOfDetectKeyPhrasesResult: TypeAlias = list[
    "aws_sdk_comprehend.types.batch_detect_key_phrases_item_result.BatchDetectKeyPhrasesItemResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDetectKeyPhrasesResult) -> list:
    import aws_sdk_comprehend.types.batch_detect_key_phrases_item_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.batch_detect_key_phrases_item_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDetectKeyPhrasesResult:
    import aws_sdk_comprehend.types.batch_detect_key_phrases_item_result

    out: ListOfDetectKeyPhrasesResult = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.batch_detect_key_phrases_item_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
