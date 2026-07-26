"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorColorSpace``."""

from typing import Literal, TypeAlias, cast

"""Video Selector Color Space"""
VideoSelectorColorSpace: TypeAlias = Literal[
    "FOLLOW",
    "HDR10",
    "HLG_2020",
    "REC_601",
    "REC_709",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelectorColorSpace) -> str:
    return value


def deserialize_json(data: str) -> VideoSelectorColorSpace:
    return cast(VideoSelectorColorSpace, data)
