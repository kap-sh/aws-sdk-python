"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpCaptionData``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Rtmp Caption Data"""
RtmpCaptionData: TypeAlias = Literal[
    "ALL",
    "FIELD1_608",
    "FIELD1_AND_FIELD2_608",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "FIELD1_608",
        "FIELD1_AND_FIELD2_608",
    )
)


def serialize_json(value: RtmpCaptionData) -> str:
    return value


def deserialize_json(data: str) -> RtmpCaptionData:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RtmpCaptionData value: {data!r}")
    return cast(RtmpCaptionData, data)
