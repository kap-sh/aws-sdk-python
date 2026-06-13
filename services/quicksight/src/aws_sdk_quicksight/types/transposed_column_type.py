"""Generated from Smithy shape ``com.amazonaws.quicksight#TransposedColumnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TransposedColumnType: TypeAlias = Literal[
    "ROW_HEADER_COLUMN",
    "VALUE_COLUMN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROW_HEADER_COLUMN",
        "VALUE_COLUMN",
    )
)


def serialize_json(value: TransposedColumnType) -> str:
    return value


def deserialize_json(data: str) -> TransposedColumnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransposedColumnType value: {data!r}")
    return cast(TransposedColumnType, data)
