"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnRole``."""

from typing import Literal, TypeAlias, cast

ColumnRole: TypeAlias = Literal[
    "DIMENSION",
    "MEASURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnRole) -> str:
    return value


def deserialize_json(data: str) -> ColumnRole:
    return cast(ColumnRole, data)
