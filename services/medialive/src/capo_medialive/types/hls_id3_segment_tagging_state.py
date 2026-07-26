"""Generated from Smithy shape ``com.amazonaws.medialive#HlsId3SegmentTaggingState``."""

from typing import Literal, TypeAlias, cast

"""State of HLS ID3 Segment Tagging"""
HlsId3SegmentTaggingState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsId3SegmentTaggingState) -> str:
    return value


def deserialize_json(data: str) -> HlsId3SegmentTaggingState:
    return cast(HlsId3SegmentTaggingState, data)
