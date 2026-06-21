"""Generated from Smithy shape ``com.amazonaws.medialive#ColorSpace``."""

from typing import Literal, TypeAlias, cast

"""Property of colorCorrections. When you are using 3D LUT files to perform color conversion on video, these are the supported color spaces."""
ColorSpace: TypeAlias = Literal[
    "HDR10",
    "HLG_2020",
    "REC_601",
    "REC_709",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColorSpace) -> str:
    return value


def deserialize_json(data: str) -> ColorSpace:
    return cast(ColorSpace, data)
