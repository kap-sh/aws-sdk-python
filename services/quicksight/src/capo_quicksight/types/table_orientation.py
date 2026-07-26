"""Generated from Smithy shape ``com.amazonaws.quicksight#TableOrientation``."""

from typing import Literal, TypeAlias, cast

TableOrientation: TypeAlias = Literal[
    "VERTICAL",
    "HORIZONTAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableOrientation) -> str:
    return value


def deserialize_json(data: str) -> TableOrientation:
    return cast(TableOrientation, data)
