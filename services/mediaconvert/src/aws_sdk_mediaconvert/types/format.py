"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

Format: TypeAlias = Literal[
    "mp4",
    "quicktime",
    "matroska",
    "webm",
    "mxf",
    "wave",
    "avi",
    "mpegts",
    "mpegps",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "mp4",
        "quicktime",
        "matroska",
        "webm",
        "mxf",
        "wave",
        "avi",
        "mpegts",
        "mpegps",
    )
)


def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Format value: {data!r}")
    return cast(Format, data)
