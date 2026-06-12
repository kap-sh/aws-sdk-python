"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAudioInterval``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Audio Interval"""
M2tsAudioInterval: TypeAlias = Literal[
    "VIDEO_AND_FIXED_INTERVALS",
    "VIDEO_INTERVAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VIDEO_AND_FIXED_INTERVALS",
        "VIDEO_INTERVAL",
    )
)


def serialize_json(value: M2tsAudioInterval) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioInterval:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsAudioInterval value: {data!r}")
    return cast(M2tsAudioInterval, data)
