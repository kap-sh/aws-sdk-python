"""Generated from Smithy shape ``com.amazonaws.quicksight#TransposedColumnType``."""

from typing import Literal, TypeAlias, cast

TransposedColumnType: TypeAlias = Literal[
    "ROW_HEADER_COLUMN",
    "VALUE_COLUMN",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransposedColumnType) -> str:
    return value


def deserialize_json(data: str) -> TransposedColumnType:
    return cast(TransposedColumnType, data)
