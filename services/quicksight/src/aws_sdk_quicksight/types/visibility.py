"""Generated from Smithy shape ``com.amazonaws.quicksight#Visibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

Visibility: TypeAlias = Literal[
    "HIDDEN",
    "VISIBLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIDDEN",
        "VISIBLE",
    )
)


def serialize_json(value: Visibility) -> str:
    return value


def deserialize_json(data: str) -> Visibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Visibility value: {data!r}")
    return cast(Visibility, data)
