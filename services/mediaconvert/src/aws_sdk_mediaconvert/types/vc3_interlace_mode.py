"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vc3InterlaceMode``."""

from typing import Literal, TypeAlias, cast

"""Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output."""
Vc3InterlaceMode: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Vc3InterlaceMode) -> str:
    return value


def deserialize_json(data: str) -> Vc3InterlaceMode:
    return cast(Vc3InterlaceMode, data)
