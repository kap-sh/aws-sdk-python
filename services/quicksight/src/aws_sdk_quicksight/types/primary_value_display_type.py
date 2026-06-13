"""Generated from Smithy shape ``com.amazonaws.quicksight#PrimaryValueDisplayType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PrimaryValueDisplayType: TypeAlias = Literal[
    "HIDDEN",
    "COMPARISON",
    "ACTUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIDDEN",
        "COMPARISON",
        "ACTUAL",
    )
)


def serialize_json(value: PrimaryValueDisplayType) -> str:
    return value


def deserialize_json(data: str) -> PrimaryValueDisplayType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrimaryValueDisplayType value: {data!r}")
    return cast(PrimaryValueDisplayType, data)
