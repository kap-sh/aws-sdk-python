"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ContainerType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ContainerType) -> str:
    return value


def deserialize_json(data: str) -> ContainerType:
    return cast(ContainerType, data)
