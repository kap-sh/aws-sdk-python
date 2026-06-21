"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#VideoFormat``."""

from typing import Literal, TypeAlias, cast

VideoFormat: TypeAlias = Literal[
    "mkv",
    "mov",
    "mp4",
    "webm",
    "flv",
    "mpeg",
    "mpg",
    "wmv",
    "three_gp",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoFormat) -> str:
    return value


def deserialize_json(data: str) -> VideoFormat:
    return cast(VideoFormat, data)
