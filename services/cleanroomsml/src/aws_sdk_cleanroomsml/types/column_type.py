"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ColumnType``."""

from typing import Literal, TypeAlias, cast

ColumnType: TypeAlias = Literal[
    "USER_ID",
    "ITEM_ID",
    "TIMESTAMP",
    "CATEGORICAL_FEATURE",
    "NUMERICAL_FEATURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnType) -> str:
    return value


def deserialize_json(data: str) -> ColumnType:
    return cast(ColumnType, data)
