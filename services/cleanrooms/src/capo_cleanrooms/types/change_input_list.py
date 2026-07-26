"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.change_input

ChangeInputList: TypeAlias = list["capo_cleanrooms.types.change_input.ChangeInput"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeInputList) -> list:
    import capo_cleanrooms.types.change_input

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.change_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeInputList:
    import capo_cleanrooms.types.change_input

    out: ChangeInputList = []
    for item in data:
        out.append(capo_cleanrooms.types.change_input.deserialize_json(item))
    return out
