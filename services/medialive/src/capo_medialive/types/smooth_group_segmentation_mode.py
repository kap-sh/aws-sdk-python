"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupSegmentationMode``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Segmentation Mode"""
SmoothGroupSegmentationMode: TypeAlias = Literal[
    "USE_INPUT_SEGMENTATION",
    "USE_SEGMENT_DURATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupSegmentationMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupSegmentationMode:
    return cast(SmoothGroupSegmentationMode, data)
