"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

"""Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default."""
Mpeg2SceneChangeDetect: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2SceneChangeDetect:
    return cast(Mpeg2SceneChangeDetect, data)
