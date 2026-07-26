"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kProfileCodecProfile``."""

from typing import Literal, TypeAlias, cast

"""Specify the codec profile for this output. Choose High, 8-bit, 4:2:0 (HIGH) or High, 10-bit, 4:2:2 (HIGH_422). These profiles are specified in ITU-T H.264."""
Xavc4kProfileCodecProfile: TypeAlias = Literal[
    "HIGH",
    "HIGH_422",
]


# --- restJson1 ser/de ---
def serialize_json(value: Xavc4kProfileCodecProfile) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kProfileCodecProfile:
    return cast(Xavc4kProfileCodecProfile, data)
