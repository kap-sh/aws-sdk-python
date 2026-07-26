"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color

ColorList: TypeAlias = list["capo_quicksight.types.hex_color.HexColor"]


# --- restJson1 ser/de ---
def serialize_json(value: ColorList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColorList:
    return list(data)
