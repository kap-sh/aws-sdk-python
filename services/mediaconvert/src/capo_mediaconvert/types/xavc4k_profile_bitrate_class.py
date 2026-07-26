"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kProfileBitrateClass``."""

from typing import Literal, TypeAlias, cast

"""Specify the XAVC 4k (Long GOP) Bitrate Class to set the bitrate of your output. Outputs of the same class have similar image quality over the operating points that are valid for that class."""
Xavc4kProfileBitrateClass: TypeAlias = Literal[
    "BITRATE_CLASS_100",
    "BITRATE_CLASS_140",
    "BITRATE_CLASS_200",
]


# --- restJson1 ser/de ---
def serialize_json(value: Xavc4kProfileBitrateClass) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kProfileBitrateClass:
    return cast(Xavc4kProfileBitrateClass, data)
