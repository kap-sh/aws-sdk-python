"""Generated from Smithy shape ``com.amazonaws.finspacedata#ColumnDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Data type of a column."""
ColumnDataType: TypeAlias = Literal[
    "STRING",
    "CHAR",
    "INTEGER",
    "TINYINT",
    "SMALLINT",
    "BIGINT",
    "FLOAT",
    "DOUBLE",
    "DATE",
    "DATETIME",
    "BOOLEAN",
    "BINARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "CHAR",
        "INTEGER",
        "TINYINT",
        "SMALLINT",
        "BIGINT",
        "FLOAT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "BOOLEAN",
        "BINARY",
    )
)


def serialize_json(value: ColumnDataType) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnDataType value: {data!r}")
    return cast(ColumnDataType, data)
