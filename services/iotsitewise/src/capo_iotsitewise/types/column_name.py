"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnName``."""

from typing import Literal, TypeAlias, cast

ColumnName: TypeAlias = Literal[
    "ALIAS",
    "ASSET_ID",
    "PROPERTY_ID",
    "DATA_TYPE",
    "TIMESTAMP_SECONDS",
    "TIMESTAMP_NANO_OFFSET",
    "QUALITY",
    "VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnName) -> str:
    return value


def deserialize_json(data: str) -> ColumnName:
    return cast(ColumnName, data)
