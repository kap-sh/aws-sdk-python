"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ColumnDataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "DECIMAL",
    "DATETIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "INTEGER",
        "DECIMAL",
        "DATETIME",
    )
)


def serialize_json(value: ColumnDataType) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnDataType value: {data!r}")
    return cast(ColumnDataType, data)
