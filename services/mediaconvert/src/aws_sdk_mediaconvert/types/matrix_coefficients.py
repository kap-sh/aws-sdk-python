"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MatrixCoefficients``."""

from typing import Literal, TypeAlias, cast

"""The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes."""
MatrixCoefficients: TypeAlias = Literal[
    "RGB",
    "ITU_709",
    "UNSPECIFIED",
    "RESERVED",
    "FCC",
    "ITU_470BG",
    "SMPTE_170M",
    "SMPTE_240M",
    "YCgCo",
    "ITU_2020_NCL",
    "ITU_2020_CL",
    "SMPTE_2085",
    "CD_NCL",
    "CD_CL",
    "ITU_2100ICtCp",
    "IPT",
    "EBU3213",
    "LAST",
]


# --- restJson1 ser/de ---
def serialize_json(value: MatrixCoefficients) -> str:
    return value


def deserialize_json(data: str) -> MatrixCoefficients:
    return cast(MatrixCoefficients, data)
