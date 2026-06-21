"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTagName``."""

from typing import Literal, TypeAlias, cast

ColumnTagName: TypeAlias = Literal[
    "COLUMN_GEOGRAPHIC_ROLE",
    "COLUMN_DESCRIPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTagName) -> str:
    return value


def deserialize_json(data: str) -> ColumnTagName:
    return cast(ColumnTagName, data)
