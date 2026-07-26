"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDetectEntitiesResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.batch_detect_entities_item_result

ListOfDetectEntitiesResult: TypeAlias = list[
    "capo_comprehend.types.batch_detect_entities_item_result.BatchDetectEntitiesItemResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDetectEntitiesResult) -> list:
    import capo_comprehend.types.batch_detect_entities_item_result

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.batch_detect_entities_item_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDetectEntitiesResult:
    import capo_comprehend.types.batch_detect_entities_item_result

    out: ListOfDetectEntitiesResult = []
    for item in data:
        out.append(
            capo_comprehend.types.batch_detect_entities_item_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
