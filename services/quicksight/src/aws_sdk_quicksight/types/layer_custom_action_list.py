"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerCustomActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.layer_custom_action

LayerCustomActionList: TypeAlias = list[
    "aws_sdk_quicksight.types.layer_custom_action.LayerCustomAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: LayerCustomActionList) -> list:
    import aws_sdk_quicksight.types.layer_custom_action

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.layer_custom_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayerCustomActionList:
    import aws_sdk_quicksight.types.layer_custom_action

    out: LayerCustomActionList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.layer_custom_action.deserialize_json(item))
    return out
