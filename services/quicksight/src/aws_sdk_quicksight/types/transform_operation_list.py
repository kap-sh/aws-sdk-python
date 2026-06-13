"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.transform_operation

TransformOperationList: TypeAlias = list[
    "aws_sdk_quicksight.types.transform_operation.TransformOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransformOperationList) -> list:
    import aws_sdk_quicksight.types.transform_operation

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.transform_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> TransformOperationList:
    import aws_sdk_quicksight.types.transform_operation

    out: TransformOperationList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.transform_operation.deserialize_json(item))
    return out
