"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3PhaseControl``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Phase Control"""
Eac3PhaseControl: TypeAlias = Literal[
    "NO_SHIFT",
    "SHIFT_90_DEGREES",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3PhaseControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3PhaseControl:
    return cast(Eac3PhaseControl, data)
