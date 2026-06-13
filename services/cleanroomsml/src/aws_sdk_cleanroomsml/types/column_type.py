"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ColumnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

ColumnType: TypeAlias = Literal[
    "USER_ID",
    "ITEM_ID",
    "TIMESTAMP",
    "CATEGORICAL_FEATURE",
    "NUMERICAL_FEATURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_ID",
        "ITEM_ID",
        "TIMESTAMP",
        "CATEGORICAL_FEATURE",
        "NUMERICAL_FEATURE",
    )
)


def serialize_json(value: ColumnType) -> str:
    return value


def deserialize_json(data: str) -> ColumnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnType value: {data!r}")
    return cast(ColumnType, data)
