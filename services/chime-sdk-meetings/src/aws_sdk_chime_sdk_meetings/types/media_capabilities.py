"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#MediaCapabilities``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

MediaCapabilities: TypeAlias = Literal[
    "SendReceive",
    "Send",
    "Receive",
    "None",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SendReceive",
        "Send",
        "Receive",
        "None",
    )
)


def serialize_json(value: MediaCapabilities) -> str:
    return value


def deserialize_json(data: str) -> MediaCapabilities:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaCapabilities value: {data!r}")
    return cast(MediaCapabilities, data)
