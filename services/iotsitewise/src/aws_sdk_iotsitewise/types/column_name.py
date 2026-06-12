"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ALIAS",
        "ASSET_ID",
        "PROPERTY_ID",
        "DATA_TYPE",
        "TIMESTAMP_SECONDS",
        "TIMESTAMP_NANO_OFFSET",
        "QUALITY",
        "VALUE",
    )
)


def serialize_json(value: ColumnName) -> str:
    return value


def deserialize_json(data: str) -> ColumnName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnName value: {data!r}")
    return cast(ColumnName, data)
