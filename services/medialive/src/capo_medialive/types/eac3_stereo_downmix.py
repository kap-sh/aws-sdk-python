"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3StereoDownmix``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Stereo Downmix"""
Eac3StereoDownmix: TypeAlias = Literal[
    "DPL2",
    "LO_RO",
    "LT_RT",
    "NOT_INDICATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3StereoDownmix) -> str:
    return value


def deserialize_json(data: str) -> Eac3StereoDownmix:
    return cast(Eac3StereoDownmix, data)
