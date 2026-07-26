"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

"""Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode."""
Ac3LfeFilter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Ac3LfeFilter:
    return cast(Ac3LfeFilter, data)
