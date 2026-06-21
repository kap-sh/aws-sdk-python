"""Generated from Smithy shape ``com.amazonaws.finspacedata#ColumnDataType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ColumnDataType) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataType:
    return cast(ColumnDataType, data)
