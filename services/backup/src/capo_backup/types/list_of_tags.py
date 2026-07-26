"""Generated from Smithy shape ``com.amazonaws.backup#ListOfTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.condition

ListOfTags: TypeAlias = list["capo_backup.types.condition.Condition"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTags) -> list:
    import capo_backup.types.condition

    out: list = []
    for item in value:
        out.append(capo_backup.types.condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTags:
    import capo_backup.types.condition

    out: ListOfTags = []
    for item in data:
        out.append(capo_backup.types.condition.deserialize_json(item))
    return out
