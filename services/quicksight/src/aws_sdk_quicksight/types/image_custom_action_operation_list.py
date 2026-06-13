"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageCustomActionOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.image_custom_action_operation

ImageCustomActionOperationList: TypeAlias = list[
    "aws_sdk_quicksight.types.image_custom_action_operation.ImageCustomActionOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageCustomActionOperationList) -> list:
    import aws_sdk_quicksight.types.image_custom_action_operation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.image_custom_action_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ImageCustomActionOperationList:
    import aws_sdk_quicksight.types.image_custom_action_operation

    out: ImageCustomActionOperationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.image_custom_action_operation.deserialize_json(
                item
            )
        )
    return out
