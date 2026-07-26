"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpAdMarkers``."""

from typing import Literal, TypeAlias, cast

"""Rtmp Ad Markers"""
RtmpAdMarkers: TypeAlias = Literal["ON_CUE_POINT_SCTE35",]


# --- restJson1 ser/de ---
def serialize_json(value: RtmpAdMarkers) -> str:
    return value


def deserialize_json(data: str) -> RtmpAdMarkers:
    return cast(RtmpAdMarkers, data)
