"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiOutputTimecodeSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

NdiOutputTimecodeSource: TypeAlias = Literal[
    "EMBEDDED_TIMECODE",
    "UTC_SYSTEM_TIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMBEDDED_TIMECODE",
        "UTC_SYSTEM_TIME",
    )
)


def serialize_json(value: NdiOutputTimecodeSource) -> str:
    return value


def deserialize_json(data: str) -> NdiOutputTimecodeSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NdiOutputTimecodeSource value: {data!r}")
    return cast(NdiOutputTimecodeSource, data)
