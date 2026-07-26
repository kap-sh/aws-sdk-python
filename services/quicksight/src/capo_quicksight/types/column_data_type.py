"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnDataType``."""

from typing import Literal, TypeAlias, cast

ColumnDataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "DECIMAL",
    "DATETIME",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnDataType) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataType:
    return cast(ColumnDataType, data)
