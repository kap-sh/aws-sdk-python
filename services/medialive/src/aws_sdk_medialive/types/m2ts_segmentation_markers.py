"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsSegmentationMarkers``."""

from typing import Literal, TypeAlias, cast

"""M2ts Segmentation Markers"""
M2tsSegmentationMarkers: TypeAlias = Literal[
    "EBP",
    "EBP_LEGACY",
    "NONE",
    "PSI_SEGSTART",
    "RAI_ADAPT",
    "RAI_SEGSTART",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsSegmentationMarkers) -> str:
    return value


def deserialize_json(data: str) -> M2tsSegmentationMarkers:
    return cast(M2tsSegmentationMarkers, data)
