"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnOrderingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ColumnOrderingType: TypeAlias = Literal[
    "GREATER_IS_BETTER",
    "LESSER_IS_BETTER",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_IS_BETTER",
        "LESSER_IS_BETTER",
        "SPECIFIED",
    )
)


def serialize_json(value: ColumnOrderingType) -> str:
    return value


def deserialize_json(data: str) -> ColumnOrderingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnOrderingType value: {data!r}")
    return cast(ColumnOrderingType, data)
