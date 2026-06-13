"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLinePatternType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ReferenceLinePatternType: TypeAlias = Literal[
    "SOLID",
    "DASHED",
    "DOTTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOLID",
        "DASHED",
        "DOTTED",
    )
)


def serialize_json(value: ReferenceLinePatternType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLinePatternType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReferenceLinePatternType value: {data!r}")
    return cast(ReferenceLinePatternType, data)
