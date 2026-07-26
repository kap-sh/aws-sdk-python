"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3PhaseControl``."""

from typing import Literal, TypeAlias, cast

"""Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode."""
Eac3PhaseControl: TypeAlias = Literal[
    "SHIFT_90_DEGREES",
    "NO_SHIFT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3PhaseControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3PhaseControl:
    return cast(Eac3PhaseControl, data)
