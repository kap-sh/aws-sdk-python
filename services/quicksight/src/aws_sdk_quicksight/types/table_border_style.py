"""Generated from Smithy shape ``com.amazonaws.quicksight#TableBorderStyle``."""

from typing import Literal, TypeAlias, cast

TableBorderStyle: TypeAlias = Literal[
    "NONE",
    "SOLID",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableBorderStyle) -> str:
    return value


def deserialize_json(data: str) -> TableBorderStyle:
    return cast(TableBorderStyle, data)
