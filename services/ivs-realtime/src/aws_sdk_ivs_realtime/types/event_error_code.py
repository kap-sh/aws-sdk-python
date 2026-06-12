"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#EventErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

EventErrorCode: TypeAlias = Literal[
    "INSUFFICIENT_CAPABILITIES",
    "QUOTA_EXCEEDED",
    "PUBLISHER_NOT_FOUND",
    "BITRATE_EXCEEDED",
    "RESOLUTION_EXCEEDED",
    "STREAM_DURATION_EXCEEDED",
    "INVALID_AUDIO_CODEC",
    "INVALID_VIDEO_CODEC",
    "INVALID_PROTOCOL",
    "INVALID_STREAM_KEY",
    "REUSE_OF_STREAM_KEY",
    "B_FRAME_PRESENT",
    "INVALID_INPUT",
    "INTERNAL_SERVER_EXCEPTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSUFFICIENT_CAPABILITIES",
        "QUOTA_EXCEEDED",
        "PUBLISHER_NOT_FOUND",
        "BITRATE_EXCEEDED",
        "RESOLUTION_EXCEEDED",
        "STREAM_DURATION_EXCEEDED",
        "INVALID_AUDIO_CODEC",
        "INVALID_VIDEO_CODEC",
        "INVALID_PROTOCOL",
        "INVALID_STREAM_KEY",
        "REUSE_OF_STREAM_KEY",
        "B_FRAME_PRESENT",
        "INVALID_INPUT",
        "INTERNAL_SERVER_EXCEPTION",
    )
)


def serialize_json(value: EventErrorCode) -> str:
    return value


def deserialize_json(data: str) -> EventErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventErrorCode value: {data!r}")
    return cast(EventErrorCode, data)
