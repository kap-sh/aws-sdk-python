"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#VideoFillMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

VideoFillMode: TypeAlias = Literal[
    "FILL",
    "COVER",
    "CONTAIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILL",
        "COVER",
        "CONTAIN",
    )
)


def serialize_json(value: VideoFillMode) -> str:
    return value


def deserialize_json(data: str) -> VideoFillMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoFillMode value: {data!r}")
    return cast(VideoFillMode, data)
