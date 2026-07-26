"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupSparseTrackType``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Sparse Track Type"""
SmoothGroupSparseTrackType: TypeAlias = Literal[
    "NONE",
    "SCTE_35",
    "SCTE_35_WITHOUT_SEGMENTATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupSparseTrackType) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupSparseTrackType:
    return cast(SmoothGroupSparseTrackType, data)
