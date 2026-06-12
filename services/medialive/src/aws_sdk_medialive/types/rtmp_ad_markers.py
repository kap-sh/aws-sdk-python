"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpAdMarkers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Rtmp Ad Markers"""
RtmpAdMarkers: TypeAlias = Literal["ON_CUE_POINT_SCTE35",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ON_CUE_POINT_SCTE35",))


def serialize_json(value: RtmpAdMarkers) -> str:
    return value


def deserialize_json(data: str) -> RtmpAdMarkers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RtmpAdMarkers value: {data!r}")
    return cast(RtmpAdMarkers, data)
