"""Generated from Smithy shape ``com.amazonaws.quicksight#RelativeDateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RelativeDateType: TypeAlias = Literal[
    "PREVIOUS",
    "THIS",
    "LAST",
    "NOW",
    "NEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREVIOUS",
        "THIS",
        "LAST",
        "NOW",
        "NEXT",
    )
)


def serialize_json(value: RelativeDateType) -> str:
    return value


def deserialize_json(data: str) -> RelativeDateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelativeDateType value: {data!r}")
    return cast(RelativeDateType, data)
