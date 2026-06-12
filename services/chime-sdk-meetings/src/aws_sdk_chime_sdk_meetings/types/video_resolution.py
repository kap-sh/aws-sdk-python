"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#VideoResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

VideoResolution: TypeAlias = Literal[
    "None",
    "HD",
    "FHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "HD",
        "FHD",
    )
)


def serialize_json(value: VideoResolution) -> str:
    return value


def deserialize_json(data: str) -> VideoResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoResolution value: {data!r}")
    return cast(VideoResolution, data)
