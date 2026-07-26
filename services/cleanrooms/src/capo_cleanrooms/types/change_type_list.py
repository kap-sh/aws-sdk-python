"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.change_type

ChangeTypeList: TypeAlias = list["capo_cleanrooms.types.change_type.ChangeType"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeTypeList) -> list:
    import capo_cleanrooms.types.change_type

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.change_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeTypeList:
    import capo_cleanrooms.types.change_type

    out: ChangeTypeList = []
    for item in data:
        out.append(capo_cleanrooms.types.change_type.deserialize_json(item))
    return out
