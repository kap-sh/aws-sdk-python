"""Generated from Smithy shape ``com.amazonaws.quicksight#FontList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.font

FontList: TypeAlias = list["capo_quicksight.types.font.Font"]


# --- restJson1 ser/de ---
def serialize_json(value: FontList) -> list:
    import capo_quicksight.types.font

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.font.serialize_json(item))
    return out


def deserialize_json(data: list) -> FontList:
    import capo_quicksight.types.font

    out: FontList = []
    for item in data:
        out.append(capo_quicksight.types.font.deserialize_json(item))
    return out
