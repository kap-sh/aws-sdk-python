"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.change

ChangeList: TypeAlias = list["capo_cleanrooms.types.change.Change"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeList) -> list:
    import capo_cleanrooms.types.change

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.change.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeList:
    import capo_cleanrooms.types.change

    out: ChangeList = []
    for item in data:
        out.append(capo_cleanrooms.types.change.deserialize_json(item))
    return out
