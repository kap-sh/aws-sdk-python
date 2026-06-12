"""Generated from Smithy shape ``com.amazonaws.pinpoint#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "ALL",
    "ANY",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ANY",
        "NONE",
    )
)


def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
