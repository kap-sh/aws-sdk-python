"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacVbrQuality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html#aac_vbr"""
AacVbrQuality: TypeAlias = Literal[
    "LOW",
    "MEDIUM_LOW",
    "MEDIUM_HIGH",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM_LOW",
        "MEDIUM_HIGH",
        "HIGH",
    )
)


def serialize_json(value: AacVbrQuality) -> str:
    return value


def deserialize_json(data: str) -> AacVbrQuality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacVbrQuality value: {data!r}")
    return cast(AacVbrQuality, data)
