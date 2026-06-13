"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Range``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

Range: TypeAlias = Literal[
    "NARROW",
    "FULL",
    "FULLPROTECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NARROW",
        "FULL",
        "FULLPROTECT",
    )
)


def serialize_json(value: Range) -> str:
    return value


def deserialize_json(data: str) -> Range:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Range value: {data!r}")
    return cast(Range, data)
