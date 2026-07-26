"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string

ActionList: TypeAlias = list["capo_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionList:
    return list(data)
