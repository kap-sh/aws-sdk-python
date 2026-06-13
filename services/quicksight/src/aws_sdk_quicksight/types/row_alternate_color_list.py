"""Generated from Smithy shape ``com.amazonaws.quicksight#RowAlternateColorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color

RowAlternateColorList: TypeAlias = list["aws_sdk_quicksight.types.hex_color.HexColor"]


# --- restJson1 ser/de ---
def serialize_json(value: RowAlternateColorList) -> list:
    return list(value)


def deserialize_json(data: list) -> RowAlternateColorList:
    return list(data)
