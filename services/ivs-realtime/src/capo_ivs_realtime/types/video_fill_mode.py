"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#VideoFillMode``."""

from typing import Literal, TypeAlias, cast

VideoFillMode: TypeAlias = Literal[
    "FILL",
    "COVER",
    "CONTAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoFillMode) -> str:
    return value


def deserialize_json(data: str) -> VideoFillMode:
    return cast(VideoFillMode, data)
