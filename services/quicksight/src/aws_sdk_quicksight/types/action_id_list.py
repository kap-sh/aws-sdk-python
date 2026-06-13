"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_id

ActionIdList: TypeAlias = list["aws_sdk_quicksight.types.action_id.ActionId"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionIdList:
    return list(data)
