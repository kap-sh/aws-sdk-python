"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnDataSubType``."""

from typing import Literal, TypeAlias, cast

ColumnDataSubType: TypeAlias = Literal[
    "FLOAT",
    "FIXED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnDataSubType) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataSubType:
    return cast(ColumnDataSubType, data)
