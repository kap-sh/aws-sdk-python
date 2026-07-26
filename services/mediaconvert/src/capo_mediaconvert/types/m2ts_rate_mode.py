"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsRateMode``."""

from typing import Literal, TypeAlias, cast

"""When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate."""
M2tsRateMode: TypeAlias = Literal[
    "VBR",
    "CBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsRateMode) -> str:
    return value


def deserialize_json(data: str) -> M2tsRateMode:
    return cast(M2tsRateMode, data)
