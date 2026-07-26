"""Generated from Smithy shape ``com.amazonaws.medialive#H264Profile``."""

from typing import Literal, TypeAlias, cast

"""H264 Profile"""
H264Profile: TypeAlias = Literal[
    "BASELINE",
    "HIGH",
    "HIGH_10BIT",
    "HIGH_422",
    "HIGH_422_10BIT",
    "MAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264Profile) -> str:
    return value


def deserialize_json(data: str) -> H264Profile:
    return cast(H264Profile, data)
