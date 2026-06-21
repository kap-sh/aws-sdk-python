"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamType``."""

from typing import Literal, TypeAlias, cast

MediaStreamType: TypeAlias = Literal[
    "video",
    "audio",
    "ancillary-data",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamType) -> str:
    return value


def deserialize_json(data: str) -> MediaStreamType:
    return cast(MediaStreamType, data)
