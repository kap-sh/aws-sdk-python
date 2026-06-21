"""Generated from Smithy shape ``com.amazonaws.medialive#HlsSegmentationMode``."""

from typing import Literal, TypeAlias, cast

"""Hls Segmentation Mode"""
HlsSegmentationMode: TypeAlias = Literal[
    "USE_INPUT_SEGMENTATION",
    "USE_SEGMENT_DURATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsSegmentationMode) -> str:
    return value


def deserialize_json(data: str) -> HlsSegmentationMode:
    return cast(HlsSegmentationMode, data)
