"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpCaptionData``."""

from typing import Literal, TypeAlias, cast

"""Rtmp Caption Data"""
RtmpCaptionData: TypeAlias = Literal[
    "ALL",
    "FIELD1_608",
    "FIELD1_AND_FIELD2_608",
]


# --- restJson1 ser/de ---
def serialize_json(value: RtmpCaptionData) -> str:
    return value


def deserialize_json(data: str) -> RtmpCaptionData:
    return cast(RtmpCaptionData, data)
