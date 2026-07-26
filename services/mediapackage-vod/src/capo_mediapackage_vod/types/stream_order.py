"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#StreamOrder``."""

from typing import Literal, TypeAlias, cast

StreamOrder: TypeAlias = Literal[
    "ORIGINAL",
    "VIDEO_BITRATE_ASCENDING",
    "VIDEO_BITRATE_DESCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamOrder) -> str:
    return value


def deserialize_json(data: str) -> StreamOrder:
    return cast(StreamOrder, data)
