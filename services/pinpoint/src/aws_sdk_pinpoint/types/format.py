"""Generated from Smithy shape ``com.amazonaws.pinpoint#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Format: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSON",
    )
)


def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Format value: {data!r}")
    return cast(Format, data)
