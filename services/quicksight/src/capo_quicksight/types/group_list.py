"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.group

GroupList: TypeAlias = list["capo_quicksight.types.group.Group"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupList) -> list:
    import capo_quicksight.types.group

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.group.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupList:
    import capo_quicksight.types.group

    out: GroupList = []
    for item in data:
        out.append(capo_quicksight.types.group.deserialize_json(item))
    return out
