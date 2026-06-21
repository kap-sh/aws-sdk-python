"""Generated from Smithy shape ``com.amazonaws.quicksight#InputColumnDataType``."""

from typing import Literal, TypeAlias, cast

InputColumnDataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "DECIMAL",
    "DATETIME",
    "BIT",
    "BOOLEAN",
    "JSON",
    "SEMISTRUCT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputColumnDataType) -> str:
    return value


def deserialize_json(data: str) -> InputColumnDataType:
    return cast(InputColumnDataType, data)
