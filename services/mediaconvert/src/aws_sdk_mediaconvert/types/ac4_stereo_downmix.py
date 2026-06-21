"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac4StereoDownmix``."""

from typing import Literal, TypeAlias, cast

"""Choose the preferred stereo downmix method. This setting tells the decoder how to downmix multi-channel audio to stereo during playback."""
Ac4StereoDownmix: TypeAlias = Literal[
    "NOT_INDICATED",
    "LO_RO",
    "LT_RT",
    "DPL2",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac4StereoDownmix) -> str:
    return value


def deserialize_json(data: str) -> Ac4StereoDownmix:
    return cast(Ac4StereoDownmix, data)
