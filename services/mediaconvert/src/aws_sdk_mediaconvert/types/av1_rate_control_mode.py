"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""'With AV1 outputs, for rate control mode, MediaConvert supports only quality-defined variable bitrate (QVBR). You can''t use CBR or VBR.'"""
Av1RateControlMode: TypeAlias = Literal["QVBR",]


# --- restJson1 ser/de ---
def serialize_json(value: Av1RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Av1RateControlMode:
    return cast(Av1RateControlMode, data)
