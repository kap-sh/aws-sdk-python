"""Generated from Smithy shape ``com.amazonaws.quicksight#InputColumnDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

InputColumnDataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "DECIMAL",
    "DATETIME",
    "BIT",
    "BOOLEAN",
    "JSON",
    "SEMISTRUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "INTEGER",
        "DECIMAL",
        "DATETIME",
        "BIT",
        "BOOLEAN",
        "JSON",
        "SEMISTRUCT",
    )
)


def serialize_json(value: InputColumnDataType) -> str:
    return value


def deserialize_json(data: str) -> InputColumnDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputColumnDataType value: {data!r}")
    return cast(InputColumnDataType, data)
