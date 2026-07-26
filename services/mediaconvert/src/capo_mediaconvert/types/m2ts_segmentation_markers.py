"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsSegmentationMarkers``."""

from typing import Literal, TypeAlias, cast

"""Inserts segmentation markers at each segmentation_time period. rai_segstart sets the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format."""
M2tsSegmentationMarkers: TypeAlias = Literal[
    "NONE",
    "RAI_SEGSTART",
    "RAI_ADAPT",
    "PSI_SEGSTART",
    "EBP",
    "EBP_LEGACY",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsSegmentationMarkers) -> str:
    return value


def deserialize_json(data: str) -> M2tsSegmentationMarkers:
    return cast(M2tsSegmentationMarkers, data)
