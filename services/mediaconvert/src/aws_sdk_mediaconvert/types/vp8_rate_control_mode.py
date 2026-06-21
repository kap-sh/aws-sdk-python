"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp8RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""With the VP8 codec, you can use only the variable bitrate (VBR) rate control mode."""
Vp8RateControlMode: TypeAlias = Literal["VBR",]


# --- restJson1 ser/de ---
def serialize_json(value: Vp8RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Vp8RateControlMode:
    return cast(Vp8RateControlMode, data)
