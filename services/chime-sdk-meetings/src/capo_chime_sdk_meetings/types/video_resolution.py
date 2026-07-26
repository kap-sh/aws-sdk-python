"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#VideoResolution``."""

from typing import Literal, TypeAlias, cast

VideoResolution: TypeAlias = Literal[
    "None",
    "HD",
    "FHD",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoResolution) -> str:
    return value


def deserialize_json(data: str) -> VideoResolution:
    return cast(VideoResolution, data)
