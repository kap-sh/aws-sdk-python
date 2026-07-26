"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string

GroupsList: TypeAlias = list["capo_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupsList) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupsList:
    return list(data)
