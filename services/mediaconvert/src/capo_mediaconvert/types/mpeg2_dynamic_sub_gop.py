"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2DynamicSubGop``."""

from typing import Literal, TypeAlias, cast

"""Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames."""
Mpeg2DynamicSubGop: TypeAlias = Literal[
    "ADAPTIVE",
    "STATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2DynamicSubGop) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2DynamicSubGop:
    return cast(Mpeg2DynamicSubGop, data)
