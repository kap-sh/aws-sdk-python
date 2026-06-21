"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3LfeControl``."""

from typing import Literal, TypeAlias, cast

"""When encoding 3/2 audio, controls whether the LFE channel is enabled"""
Eac3LfeControl: TypeAlias = Literal[
    "LFE",
    "NO_LFE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3LfeControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3LfeControl:
    return cast(Eac3LfeControl, data)
