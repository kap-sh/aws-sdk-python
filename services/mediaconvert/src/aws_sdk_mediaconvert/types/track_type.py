"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TrackType``."""

from typing import Literal, TypeAlias, cast

TrackType: TypeAlias = Literal[
    "video",
    "audio",
    "data",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrackType) -> str:
    return value


def deserialize_json(data: str) -> TrackType:
    return cast(TrackType, data)
