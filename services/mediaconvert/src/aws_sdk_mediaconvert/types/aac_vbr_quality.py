"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacVbrQuality``."""

from typing import Literal, TypeAlias, cast

"""Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html#aac_vbr"""
AacVbrQuality: TypeAlias = Literal[
    "LOW",
    "MEDIUM_LOW",
    "MEDIUM_HIGH",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacVbrQuality) -> str:
    return value


def deserialize_json(data: str) -> AacVbrQuality:
    return cast(AacVbrQuality, data)
