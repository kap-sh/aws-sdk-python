"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp9RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""With the VP9 codec, you can use only the variable bitrate (VBR) rate control mode."""
Vp9RateControlMode: TypeAlias = Literal["VBR",]


# --- restJson1 ser/de ---
def serialize_json(value: Vp9RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Vp9RateControlMode:
    return cast(Vp9RateControlMode, data)
