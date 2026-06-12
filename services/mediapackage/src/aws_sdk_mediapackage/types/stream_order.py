"""Generated from Smithy shape ``com.amazonaws.mediapackage#StreamOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

StreamOrder: TypeAlias = Literal[
    "ORIGINAL",
    "VIDEO_BITRATE_ASCENDING",
    "VIDEO_BITRATE_DESCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORIGINAL",
        "VIDEO_BITRATE_ASCENDING",
        "VIDEO_BITRATE_DESCENDING",
    )
)


def serialize_json(value: StreamOrder) -> str:
    return value


def deserialize_json(data: str) -> StreamOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamOrder value: {data!r}")
    return cast(StreamOrder, data)
