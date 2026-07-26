"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnOrderingType``."""

from typing import Literal, TypeAlias, cast

ColumnOrderingType: TypeAlias = Literal[
    "GREATER_IS_BETTER",
    "LESSER_IS_BETTER",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnOrderingType) -> str:
    return value


def deserialize_json(data: str) -> ColumnOrderingType:
    return cast(ColumnOrderingType, data)
