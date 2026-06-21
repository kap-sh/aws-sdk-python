"""Generated from Smithy shape ``com.amazonaws.medialive#H264QualityLevel``."""

from typing import Literal, TypeAlias, cast

"""H264 Quality Level"""
H264QualityLevel: TypeAlias = Literal[
    "ENHANCED_QUALITY",
    "STANDARD_QUALITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264QualityLevel) -> str:
    return value


def deserialize_json(data: str) -> H264QualityLevel:
    return cast(H264QualityLevel, data)
