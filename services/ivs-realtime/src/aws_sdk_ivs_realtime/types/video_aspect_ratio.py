"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#VideoAspectRatio``."""

from typing import Literal, TypeAlias, cast

VideoAspectRatio: TypeAlias = Literal[
    "AUTO",
    "VIDEO",
    "SQUARE",
    "PORTRAIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoAspectRatio) -> str:
    return value


def deserialize_json(data: str) -> VideoAspectRatio:
    return cast(VideoAspectRatio, data)
