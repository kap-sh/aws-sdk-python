"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnDataRole``."""

from typing import Literal, TypeAlias, cast

ColumnDataRole: TypeAlias = Literal[
    "DIMENSION",
    "MEASURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnDataRole) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataRole:
    return cast(ColumnDataRole, data)
