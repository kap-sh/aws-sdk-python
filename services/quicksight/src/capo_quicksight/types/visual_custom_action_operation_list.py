"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.visual_custom_action_operation

VisualCustomActionOperationList: TypeAlias = list[
    "capo_quicksight.types.visual_custom_action_operation.VisualCustomActionOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomActionOperationList) -> list:
    import capo_quicksight.types.visual_custom_action_operation

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.visual_custom_action_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VisualCustomActionOperationList:
    import capo_quicksight.types.visual_custom_action_operation

    out: VisualCustomActionOperationList = []
    for item in data:
        out.append(
            capo_quicksight.types.visual_custom_action_operation.deserialize_json(item)
        )
    return out
