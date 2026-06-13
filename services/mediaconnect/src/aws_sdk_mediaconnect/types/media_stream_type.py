"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

MediaStreamType: TypeAlias = Literal[
    "video",
    "audio",
    "ancillary-data",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "video",
        "audio",
        "ancillary-data",
    )
)


def serialize_json(value: MediaStreamType) -> str:
    return value


def deserialize_json(data: str) -> MediaStreamType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaStreamType value: {data!r}")
    return cast(MediaStreamType, data)
