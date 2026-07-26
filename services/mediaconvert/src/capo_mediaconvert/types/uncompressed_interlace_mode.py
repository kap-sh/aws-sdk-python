"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UncompressedInterlaceMode``."""

from typing import Literal, TypeAlias, cast

"""Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output."""
UncompressedInterlaceMode: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UncompressedInterlaceMode) -> str:
    return value


def deserialize_json(data: str) -> UncompressedInterlaceMode:
    return cast(UncompressedInterlaceMode, data)
