"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacRateControlMode``."""

from typing import Literal, TypeAlias, cast

"""Specify the AAC rate control mode. For a constant bitrate: Choose CBR. Your AAC output bitrate will be equal to the value that you choose for Bitrate. For a variable bitrate: Choose VBR. Your AAC output bitrate will vary according to your audio content and the value that you choose for Bitrate quality."""
AacRateControlMode: TypeAlias = Literal[
    "CBR",
    "VBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacRateControlMode) -> str:
    return value


def deserialize_json(data: str) -> AacRateControlMode:
    return cast(AacRateControlMode, data)
