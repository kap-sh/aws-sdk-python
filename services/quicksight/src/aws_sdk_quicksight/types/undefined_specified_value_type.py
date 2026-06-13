"""Generated from Smithy shape ``com.amazonaws.quicksight#UndefinedSpecifiedValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

UndefinedSpecifiedValueType: TypeAlias = Literal[
    "LEAST",
    "MOST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEAST",
        "MOST",
    )
)


def serialize_json(value: UndefinedSpecifiedValueType) -> str:
    return value


def deserialize_json(data: str) -> UndefinedSpecifiedValueType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UndefinedSpecifiedValueType value: {data!r}"
        )
    return cast(UndefinedSpecifiedValueType, data)
