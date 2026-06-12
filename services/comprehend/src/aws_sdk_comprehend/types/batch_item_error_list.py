"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchItemErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.batch_item_error

BatchItemErrorList: TypeAlias = list[
    "aws_sdk_comprehend.types.batch_item_error.BatchItemError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchItemErrorList) -> list:
    import aws_sdk_comprehend.types.batch_item_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.batch_item_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchItemErrorList:
    import aws_sdk_comprehend.types.batch_item_error

    out: BatchItemErrorList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.batch_item_error.deserialize_aws_json_1_1(item)
        )
    return out
