"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SegmentationScope``."""

from typing import Literal, TypeAlias, cast

"""Scte35 Segmentation Scope"""
Scte35SegmentationScope: TypeAlias = Literal[
    "ALL_OUTPUT_GROUPS",
    "SCTE35_ENABLED_OUTPUT_GROUPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35SegmentationScope) -> str:
    return value


def deserialize_json(data: str) -> Scte35SegmentationScope:
    return cast(Scte35SegmentationScope, data)
