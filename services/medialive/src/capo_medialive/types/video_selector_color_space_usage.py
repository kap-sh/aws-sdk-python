"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorColorSpaceUsage``."""

from typing import Literal, TypeAlias, cast

"""Video Selector Color Space Usage"""
VideoSelectorColorSpaceUsage: TypeAlias = Literal[
    "FALLBACK",
    "FORCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelectorColorSpaceUsage) -> str:
    return value


def deserialize_json(data: str) -> VideoSelectorColorSpaceUsage:
    return cast(VideoSelectorColorSpaceUsage, data)
