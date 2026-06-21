"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Format``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
