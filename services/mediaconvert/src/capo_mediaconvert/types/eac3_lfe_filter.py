"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

"""Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode."""
Eac3LfeFilter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3LfeFilter:
    return cast(Eac3LfeFilter, data)
