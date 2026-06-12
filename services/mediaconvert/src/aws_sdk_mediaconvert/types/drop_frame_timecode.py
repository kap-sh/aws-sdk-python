"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DropFrameTimecode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion or Timecode track is enabled."""
DropFrameTimecode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: DropFrameTimecode) -> str:
    return value


def deserialize_json(data: str) -> DropFrameTimecode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DropFrameTimecode value: {data!r}")
    return cast(DropFrameTimecode, data)
