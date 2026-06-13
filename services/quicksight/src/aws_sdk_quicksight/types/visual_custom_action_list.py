"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visual_custom_action

VisualCustomActionList: TypeAlias = list[
    "aws_sdk_quicksight.types.visual_custom_action.VisualCustomAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomActionList) -> list:
    import aws_sdk_quicksight.types.visual_custom_action

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.visual_custom_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> VisualCustomActionList:
    import aws_sdk_quicksight.types.visual_custom_action

    out: VisualCustomActionList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.visual_custom_action.deserialize_json(item))
    return out
