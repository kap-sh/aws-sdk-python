"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TrackType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

TrackType: TypeAlias = Literal[
    "video",
    "audio",
    "data",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "video",
        "audio",
        "data",
    )
)


def serialize_json(value: TrackType) -> str:
    return value


def deserialize_json(data: str) -> TrackType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrackType value: {data!r}")
    return cast(TrackType, data)
