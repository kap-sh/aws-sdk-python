"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ContainerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Container for this output. Some containers require a container settings object. If not specified, the default object will be created."""
ContainerType: TypeAlias = Literal[
    "F4V",
    "GIF",
    "ISMV",
    "M2TS",
    "M3U8",
    "CMFC",
    "MOV",
    "MP4",
    "MPD",
    "MXF",
    "OGG",
    "WEBM",
    "RAW",
    "Y4M",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "F4V",
        "GIF",
        "ISMV",
        "M2TS",
        "M3U8",
        "CMFC",
        "MOV",
        "MP4",
        "MPD",
        "MXF",
        "OGG",
        "WEBM",
        "RAW",
        "Y4M",
    )
)


def serialize_json(value: ContainerType) -> str:
    return value


def deserialize_json(data: str) -> ContainerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerType value: {data!r}")
    return cast(ContainerType, data)
