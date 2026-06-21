"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264WriteMp4PackagingType``."""

from typing import Literal, TypeAlias, cast

"""Specify how SPS and PPS NAL units are written in your output MP4 container, according to ISO/IEC 14496-15. If the location of these parameters doesn't matter in your workflow: Keep the default value, AVC1. MediaConvert writes SPS and PPS NAL units in the sample description ('stsd') box (but not into samples directly). To write SPS and PPS NAL units directly into samples (but not in the 'stsd' box): Choose AVC3. When you do, note that your output might not play properly with some downstream systems or players."""
H264WriteMp4PackagingType: TypeAlias = Literal[
    "AVC1",
    "AVC3",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264WriteMp4PackagingType) -> str:
    return value


def deserialize_json(data: str) -> H264WriteMp4PackagingType:
    return cast(H264WriteMp4PackagingType, data)
