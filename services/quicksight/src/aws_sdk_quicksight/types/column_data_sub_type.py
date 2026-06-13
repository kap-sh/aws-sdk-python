"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnDataSubType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ColumnDataSubType: TypeAlias = Literal[
    "FLOAT",
    "FIXED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLOAT",
        "FIXED",
    )
)


def serialize_json(value: ColumnDataSubType) -> str:
    return value


def deserialize_json(data: str) -> ColumnDataSubType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnDataSubType value: {data!r}")
    return cast(ColumnDataSubType, data)
